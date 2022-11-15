##import libraries
import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
from PIL import Image
import skimage.morphology as morph


## functions here ##
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

#Get X(Bx) values from B
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

## functions here ##

## transform to origin ####
path1="path to the location of the final pre-aligned folder i.e. rotated individual 'hooked' hair contours ready for ICP implementation"
path2="path to the location of output folder i.e. scaled and rotated individual 'hooked' hair contours centred at the origin ready for ICP implementation"

#read image
for filename in os.listdir(path1):
    print(filename)
    img = cv2.imread(os.path.join(path1,filename),0) 
    ret,thresh_img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    xImg,yImg= np.where(thresh_img>0)

    ##transform to origin
    xcd=sum(xImg)/len(xImg)
    ycd=sum(yImg)/len(yImg)

    xImg=xImg-xcd
    yImg=yImg-ycd

    #function for euclidean distance b/w 2 points
    def distance(x1,y1,x2,y2):
        d = (x1 - x2)**2 + (y1-y2)**2 
        return d

    ## find contour coords
    box,cont,largestContIdx,length_contour=makeBoundingBox(thresh_img)

    #list with contour co-ordinates
    C=[]
    for i in cont[largestContIdx]:
        C.append([i[0][0],i[0][1]])

    ##calculate distance from centroid
    D=[]
    for (a,b) in C:
        k=distance(a,b,xcd,ycd)
        D.append(k)

    ##calculate centroid size
    cs=(sum(D))**.5/len(D)

    ##make area = 1
    xImg=xImg/cs
    yImg=yImg/cs

    ##plot and save
    fig,ax =plt.subplots(1,1)
    ax=plt.scatter(yImg,xImg,color='white')
    fig.set_facecolor('black')
    plt.axis('off')
    os.chdir(path2)
    plt.savefig(filename)
    
# transform to origin ####





