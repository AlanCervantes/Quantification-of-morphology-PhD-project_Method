## calculate the area & perimeter of extracted 'hooked' hair contours and report the results in a csv file ##

#Import all libraries
import os
import cv2
from PIL import Image
from matplotlib.pyplot import contour
from skimage.measure import find_contours
import pandas as pd
import argparse
import sys


#define distance
def distance(x1,y1,x2,y2):
     d = (x1 - x2)**2 + (y1-y2)**2 
     return d

def AreaPerimeter(path1,path2):

    Filename=[]
    CSN1=[]
    NS=[]



    for filename in os.listdir(path1):
        #img = Image.open(os.path.join(path,filename)).convert('L')
        img = cv2.imread(os.path.join(path1,filename),cv2.IMREAD_GRAYSCALE)
        #red, green, blue = img.split()
        coords = find_contours(img,200)
        
        if len(coords)!=0:
            coords = coords[0]
            
            x=[i[0] for i in coords]  
            y=[i[1] for i in coords] 
            
            #centroid
            xc=sum(x)/len(x)
            yc=sum(y)/len(y)
            
            #xnew=x-xc
            #ynew=y-yc #make centroid as (0,0)
        
            coords_n=[]
            
            for i in range(0,len(coords)):
                coords_n.append([x[i],y[i]])  #store the new coordinates in a list
            

        D=[] #list to store the distances
        
        #centroid length(cl)
        for (x,y) in coords_n:
            k=distance(x,y,xc,yc)
            D.append(k)
            
        cs=(sum(D))**.5
        CSN1.append(cs)

        Filename.append(filename)

    data={'ID': Filename, 'Area':CSN1}
    NS=pd.DataFrame(data)

    #Perimeter

    LN=[] #list to store the perimeter

    for filename in os.listdir(path1):
    
        imgcolor = cv2.imread(os.path.join(path1,filename))  
        gray = cv2.cvtColor(imgcolor, cv2.COLOR_BGR2GRAY)
        ret,binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        contours,hier = cv2.findContours(binary, 1,1)

        length_contour=0
        cIdx=-1

        for idx,i in enumerate(contours):
            if len(i)>length_contour:
                length_contour=len(i)
                cIdx=idx
    
        l=cv2.arcLength(contours[cIdx],closed=True)
        LN.append(l)  ######LN!!!

    NS['Perimeter']=LN
    NS.to_csv(path2, index = False, header = True)
    
    return(NS)

### Create command line interface (CLI) ###

##create the parser
parser = argparse.ArgumentParser(description='calculate area and perimeter from path1 and save at path2')

## add arguments
parser.add_argument('path1', type=str, help='Data folder address')
parser.add_argument('path2', type=str, help='Output folder address')

## execute the parser
args = parser.parse_args()

path1=sys.argv[1]
path2=sys.argv[2]
 
#path1 to folder which has the extracted 'hooked' hair contours
#path2 to the location where you want to save the result file in csv format

AreaPerimeter(path1,path2)

















