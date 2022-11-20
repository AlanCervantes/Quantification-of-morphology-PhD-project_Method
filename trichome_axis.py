#This script was used to quantify the degree of hooking in a trichome#

## Import libraries ##
import cv2
from cv2 import line
import numpy as np
from skimage.morphology import medial_axis
import skimage.morphology as morph
import matplotlib.pyplot as plt
from scipy.interpolate import splprep, splev
import skimage.filters.rank as rank
from sklearn.linear_model import LinearRegression
import math
from scipy.stats import norm
import seaborn as sns


def makeBoundingBox(binaryImg):
    #Find contours
    contours,hierarchy = cv2.findContours(binaryImg, 1, 1)
    length_contour=0
    cIdx=-1
    for idx,i in enumerate(contours):
        if len(i)>length_contour:
            length_contour=len(i)
            cIdx=idx

    #Get coordinates of rotated bounding box
    try:
        rect1 = cv2.minAreaRect(contours[cIdx])
    except ValueError:
        print("cIdx is negative or invalid")
    box = cv2.boxPoints(rect1)

    return box,contours,cIdx,length_contour


def GetXfromI(B):
    Bx=[]
    for b in B:
        Bx.append(b[0])
    return(Bx)

#Get Y(By) values from B
def GetYfromI(B):
    By=[]
    for b in B:
        By.append(b[1])
    return (By)


def Average(lst):
    return sum(lst) / len(lst)

def midpoint(skeletonCoordsX,skeletonCoordsY):

    #Find the mid-point of the skeleton
    Skelmidx=Average(skeletonCoordsX)
    Skelmidy=Average(skeletonCoordsY)

    #print(Skelmidx,Skelmidy)

    midx=list(skeletonCoordsX).index(int(Skelmidx))
    
    #midy=skeletonCoordsY.index(int(Skelmidy))
    Skelmidy1=list(skeletonCoordsY)[midx]

    #print(Skelmidx,Skelmidy1)

    return(Skelmidx,Skelmidy1)


def trisection_skel(skeletonCoordsX,skeletonCoordsY,skel):
    #Find the number of true neighbors of the medial axis in the skeleton array
    arrBinary = np.zeros_like(skel, dtype='uint8') 
    arrBinary[skeletonCoordsX,skeletonCoordsY]=1
    
    #Find the point of trisection in the skeleton
    a = np.array([[1,1,1],
                [1,0,1],
                [1,1,1]])

    threePointsX,threePointsY=np.where(rank.sum(arrBinary,a)>=3)
    onePointX,onePointY=np.where(rank.sum(arrBinary,a)==1)
    orangePointsX=[]
    orangePointsY=[]

    for i,j in zip(threePointsX,threePointsY):
        if (i,j) in zip(skeletonCoordsX,skeletonCoordsY):
            orangePointsX.append(i)
            orangePointsY.append(j)
                        
    #Find the edge and tip of the skeleton
    greenPointsX=[]
    greenPointsY=[]

    for i,j in zip(onePointX,onePointY):
        if (i,j) in zip(skeletonCoordsX,skeletonCoordsY):
            greenPointsX.append(i)
            greenPointsY.append(j)
            
    return (greenPointsX,greenPointsY,orangePointsX,orangePointsY)


def chopskel(skeletonCoordsY,threshY,skeletonCoords):
    listy=[i for i in skeletonCoordsY if i < threshY]   
    #print(listy)     
    # make list
    chopped=[]
    for i in  listy:
        #print(i)
        for j in skeletonCoords:
            if j[0]==i:
                chopped.append(j)
    return(chopped)


def pltDataHist(hist_list_input):
    # Calculating mean and standard 
    # deviation
    # Plotting the histogram.
    
    # hist_list_input_sorted = np.sort(hist_list_input)
    hist_list_input_int_dropped = []
    hist_list_input_int = [int(hist_list_input) for hist_list_input in hist_list_input]
    counts, bins = np.histogram(hist_list_input_int)

    for i in range(len(hist_list_input_int)):
        if len(bins) > 3 and hist_list_input_int[i] >= int(bins[2]):
            hist_list_input_int_dropped.append(hist_list_input_int[i])
    return hist_list_input_int_dropped



## All functions here ##
img=cv2.imread(r"/Users/ankita/Desktop/Data/Hooking_images/trichome_commonbean.png",0)

def disthistogramT(img):
    graymodel=np.array(img)
    data = morph.binary_closing(graymodel, morph.disk(1))
    data = morph.binary_opening(data, morph.disk(1))
    data = data.astype(int)
    skel, distance = morph.medial_axis(data, return_distance=True, random_state=0)
    #Pruning.prune(skel,distance)


    box,cont,largestContIdx,length_contour=makeBoundingBox(img)

    #list with contour co-ordinates
    C=[]
    for i in cont[largestContIdx]:
        C.append([i[0][0],i[0][1]])
    
    Cx=GetXfromI(C)
    Cy=GetYfromI(C)   


    skeletonCoordsX,skeletonCoordsY=np.where(skel==True)

    ##get the point of trisection and tips of the skeleton
    greenPointsX,greenPointsY,orangePointX,orangePointY = trisection_skel(skeletonCoordsX,skeletonCoordsY,skel)

    #Make list of all skeletoncoords
    skeletonCoords=[]
    for i in range(0,len(skeletonCoordsX)):
        skeletonCoords.append((skeletonCoordsX[i],skeletonCoordsY[i]))

    ## clean skeleton ##
    chopped=chopskel(skeletonCoordsX,orangePointX[1],skeletonCoords)
    choppedX=GetXfromI(chopped)
    choppedY=GetYfromI(chopped)

    #get midpoint of clean skeleton#
    mp = midpoint(choppedX,choppedY)

    ## get fit line ##


    ##chop off skeleton##
    listx=[i for i in choppedX if i > mp[0]]   
        #print(listy)     
        # make list
    fit=[]
    for i in  listx:
        #print(i)
        for j in chopped:
            if j[0]==i:
                if j[1]<700:
                    fit.append(j)

    fitX=GetXfromI(fit)
    fitY=GetYfromI(fit)


    ## fit regression line ##
    ## Linear Regression line ##
    x = np.array(fitX).reshape((-1, 1))
    y = np.array(fitY)
    model = LinearRegression()
    model.fit(x, y)

    x_new = np.array(fitX).reshape((-1, 1))
    y_new = model.predict(x_new)

    ## find the slope and the intercept ##
    m=model.coef_
    c=model.intercept_

    ## plot the distances from every point on the skeleton to the axis ##
    def distance(point,coef):
        return abs((coef[0]*point[0])-point[1]+coef[1])/math.sqrt((coef[0]*coef[0])+1)

    dis=[]
    i=0
    ind=[]
    for j in chopped:
        d=distance(j,(m,c))
        i=i+1
        ind.append(i)
        dis.append(d[0])
        
    return (dis,skeletonCoordsX,skeletonCoordsY,choppedX,choppedY,fitX,fitY,x_new,y_new,Cx,Cy,orangePointY,orangePointX,mp)

## get the distance values ##
dis,skeletonCoordsX,skeletonCoordsY,choppedX,choppedY,fitX,fitY,x_new,y_new,Cx,Cy,orangePointY,orangePointX,mp=disthistogramT(img)



## Uncomment below to plot the norm fit and the medial axis ##


## plot histogram and fit norm ##
# hist_list_input_int_dropped = pltDataHist(dis)
# mu, std = norm.fit(hist_list_input_int_dropped) 
# _,bins,_=plt.hist(hist_list_input_int_dropped, density=True, alpha=0.6, color='r')

# #Plot the normal PDF.
# xmin, xmax = plt.xlim()
# x = np.linspace(xmin, xmax, 100)
# p = norm.pdf(x, mu, std)
# fit_curve=norm.pdf(bins,mu,std)
# plt.plot(x, p, 'k', linewidth=2)
# title = "Mean & SD: {:.2f} and {:.2f}".format(mu, std)
# plt.title(title)
# #plt.show()

# # Plot the PDF
# # ax = sns.distplot(hist_list_input_int_dropped, kde = True)
# # ax.axvline(x=mu,
# #             color='blue',
# #             ls='--', 
# #             lw=2.5)
# # title = "Mean & SD: {:.2f} and {:.2f}".format(mu, std)
# # plt.title(title)
# #plt.show()



# # plot and check axis & skeleton ##
# fig,ax =plt.subplots(1,1)
# ax.scatter(skeletonCoordsY,skeletonCoordsX)
# ax.scatter(choppedY,choppedX,color='skyblue')
# ax.scatter(fitY,fitX)
# ax.plot(y_new,x_new,linestyle='--',color='red',linewidth=3)
# ax.plot(Cx,Cy,color='black')
# ax.scatter(orangePointY,orangePointX,color='blue')
# ax.scatter(mp[1],mp[0],color='blue')
# ax.set_axis_off()
# plt.show()
## plot and check axis & skeleton ##

