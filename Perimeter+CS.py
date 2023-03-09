## calculate the area & perimeter of extracted 'hooked' hair contours and output the results as a csv file ##

## Import all libraries ##
import os
import cv2
from PIL import Image
from matplotlib.pyplot import contour
from skimage.measure import find_contours
import pandas as pd
import argparse
import sys


## calculate eculidean distance ##
def distance(x1,y1,x2,y2):
     d = (x1 - x2)**2 + (y1-y2)**2 
     return d


## fuction to quantify area & perimeter ##
def AreaPerimeter(path1,path2):

    Filename=[]   #define empty lists
    CSN1=[]
    NS=[]
    
    ## Area ##

    for filename in os.listdir(path1):
        
        print('Area'+filename)  #print filename to check code is running#
        
        img = cv2.imread(os.path.join(path1,filename),cv2.IMREAD_GRAYSCALE)  #read image
  
        coords = find_contours(img,200)  #find contour co-ordinates
        
        if len(coords)!=0:
            coords = coords[0]
            
            x=[i[0] for i in coords]  #x-cords of contour
            y=[i[1] for i in coords]  #y-coords of contour
            
            #compute centroid
            xc=sum(x)/len(x)
            yc=sum(y)/len(y)
            
        
            coords_n=[] #store the contour coordinates in a list
            
            for i in range(0,len(coords)):
                coords_n.append([x[i],y[i]])  
            

        D=[] #list to store the distances
        
       #calculate distance of all boundary points from centroid
        for (x,y) in coords_n:
            k=distance(x,y,xc,yc)
            D.append(k)
         
        #compute centroid size   
        cs=(sum(D))**.5
        CSN1.append(cs)

        #store the filenames in a list
        Filename.append(filename)


    #create a dictionary to store filename:area
    data={'ID': Filename, 'Area':CSN1}
    
    #store the dictionary as a dataframe
    NS=pd.DataFrame(data)

    ## Perimeter ##

    LN=[] #define empty list

    for filename in os.listdir(path1):
    
        print('Perimeter'+filename) #print filename to check code is running#
        
        imgcolor = cv2.imread(os.path.join(path1,filename))  #read image 
        gray = cv2.cvtColor(imgcolor, cv2.COLOR_BGR2GRAY) #make it grayscale
        ret,binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) #threshod grayscale image
        
        contours,hier = cv2.findContours(binary, 1,1) #find contour of binary image

        
        #find the index of the largest contour in the image i.e. the boundary
        length_contour=0
        cIdx=-1
        for idx,i in enumerate(contours):
            if len(i)>length_contour:
                length_contour=len(i)
                cIdx=idx
    
        l=cv2.arcLength(contours[cIdx],closed=True) #find length of the largest contour
        
        LN.append(l)  #append to the list

    NS['Perimeter']=LN #make perimeter column in NS dataframe
    
    NS.to_csv(path2, index = False, header = True) #write dataframe in csv file
    
    return(NS)

### Create command line interface (CLI) ###

##create the parser
parser = argparse.ArgumentParser(description='calculate area and perimeter from path1 and save at path2')

## add arguments
parser.add_argument('path1', type=str, help='Data folder address')
parser.add_argument('path2', type=str, help='Output folder address')

## execute the parser
args = parser.parse_args()

#inputs for the command line
path1=sys.argv[1]
path2=sys.argv[2]
 
#path1 to folder which has the extracted 'hooked' hair contours
#path2 to the location where you want to save the result file in csv format


#Run the function 
AreaPerimeter(path1,path2)

















