
### This script was used for the pre-alignment of contours prior to the implementation of ICP. The pre-aligned contours are all horizontal,
### facing downwards towards the right ###


### Import Libraries #####

import cv2
import math
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import skimage.filters.rank as rank
from skimage.morphology import medial_axis
import os
import itertools
import sys
import ICP

### Import Libraries #####

##### All functions here ######
def makelist(xList,yList):
    B=[]
    for i in range(0,len(xList)):
        B.append((xList[i],yList[i]))
    return(B)

def lineAsPointList(m, c, startX,endX,startY,endY):
    xList=np.linspace(startX,endX)
    yList=[]
    B=[]

    if abs(m) == np.Inf:
        yList=np.linspace(startY,endY)
        B=makelist(xList,yList)

    else:
        for i in xList:
            y=(m*i) + c
            yList.append(y)
            B.append([i,y])            

    return xList,yList,B


def intersection(lst1, lst2):
    lst3=[]
    for value1 in lst1:
        for value2 in lst2:
            if np.abs(value1[0]-value2[0])<1.0:
                if np.abs(value1[1]-value2[1])<1.0:
                    
                    lst3.append(value2)
    
    return lst3

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

def rotatePoints(x,y,slope):
    ###Translate and rotate the shape to make it horizontal###
    if slope > 0.: angle=math.atan(np.abs(slope))-0.03
    elif slope < 0.: angle=-math.atan(np.abs(slope))-0.03
    else: angle=0.
    
    #print(angle)

    #calculate the centroid
    xcd=sum(x)/len(x)
    ycd=sum(y)/len(y)

    #subtract the centroid 
    xT=[]
    yT=[]
    for i in range(0,len(x)):
        xT.append(x[i]-xcd)
        yT.append(y[i]-ycd)

    #Rotation matrix    
    r=[[math.cos(angle), -math.sin(angle)],[(math.sin(angle)), math.cos(angle)]]
    mr=np.matrix(r)

    #Data matrix
    pointMatrix = np.matrix(np.column_stack((xT,yT)))
    rx=(pointMatrix)*mr 
    for i in range(0,len(rx)):
        rx[i,0]+=xcd
        rx[i,1]+=ycd
    
    rx=rx.tolist()
    return rx

def LineFromPoints(P, Q):
    a = Q[1] - P[1]
    b = Q[0] - P[0]
    c=P[1] - (float(a/b)* P[0]) 
    #print(Q[0],Q[1])
    return(float(a/b),float(c))

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
# All functions here ###

## Pre-alignment #####

#Read the image 
path="path to the location of input folder i.e. extracted individual 'hooked' hair contours"
path1="path to the location to save the output folder i.e. rotated contours horizontal to the X-axis"

# # ## make all shapes horizontal ###### ##
# ##Convert to binary image

for filename in os.listdir(path):  

    print(filename)   
    #Read the image 
    img = cv2.imread(os.path.join(path1,filename),0) 

    ret,thresh_img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    xImg,yImg= np.where(thresh_img>0)

    #Make bounding box
    box,cont,largestContIdx,length_contour=makeBoundingBox(thresh_img)

    #list with contour co-ordinates
    C=[]
    for i in cont[largestContIdx]:
        C.append([i[0][0],i[0][1]])

    #Get angle of rotation for the shape
    maxDist=0
    longSide=[[],[]]
    for corner in range(0,len(box)-1):
        #print (box[corner])
        dist = (box[corner][0]-box[corner+1][0])**2+(box[corner][1]-box[corner+1][1])**2

        if maxDist<dist:
            maxDist=dist

            longSide[0]=box[corner]
            longSide[1]=box[corner+1]

    slope,intercept=LineFromPoints(longSide[0],longSide[1])

    #Rotate shape wrt the longest edge of bounding box
    coordsRotImg=rotatePoints(GetXfromI(C),GetYfromI(C),slope)

    #### fill the contour for  shapes #######
    a3 = np.array(coordsRotImg, dtype=np.int32)
    image=cv2.fillPoly(np.ones_like(img),pts=[a3],color=(255,0,0))

    #smoothen the boundary
    kernel  = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel,iterations= 5)
    opening = cv2.dilate(opening,kernel,iterations = 1)

    #save it as a figure
    #os.chdir(r"/Users/ankita/Desktop/DataAnalysis/RGB/Control/Control_Hooking_extracted_v_filled")
    os.chdir(path1)
    cv2.imwrite(filename,image)

    ### fill the contour shapes #######

path2="path to the location of output folder i.e. extracted individual 'hooked' hair contours after noise removal"

# remove noise ###
for filename in os.listdir(path1):     
    #Read the image 
    print(filename)
    img = cv2.imread(os.path.join(path,filename),0) 
    ret,thresh_img = cv2.threshold(img,200,255,cv2.THRESH_BINARY)

    ## opening ##
    kernel = np.ones((5,5),np.uint8)
    opening = cv2.morphologyEx(thresh_img, cv2.MORPH_OPEN, kernel)
    ## opening ##

    os.chdir(path2)
    cv2.imwrite(filename,opening)
#remove noise



### This step is followed by manually separating the rotated contours into the following four groups - Right-up, Right-down, Left-up & Left-down ###

### flip the shapes for left/right group to match final orientation i.e. all right down ######

path3 = "path to the location of final pre-aligned folder i.e. oriented individual 'hooked' hair contours ready for ICP implementation"

## 20XP up left ###
path4 = "path to the location of left-up folder i.e. extracted & rotated individual 'hooked' hair contours facing upwards to the left"

for filename in os.listdir(path):
    print(filename)
    img = cv2.imread(os.path.join(path,filename),0)
    flip1 = cv2.flip(img, 0)  ## down
    flip2 = cv2.flip(flip1, 1)  ##right
    os.chdir(path3)
    cv2.imwrite(filename,flip2)
## 20XP up left ###

## 20XP down left ###"path to the location of right-down folder i.e. extracted & rotated individual 'hooked' hair contours facing downwards to the right"(r"/Users/ankita/Desktop/DataAnalysis/RGB/Procrustes/Re-analysis/Pre-aligned_reanalysis/NStress/Left/Left_down")
path5 = "path to the location of left-down folder i.e. extracted & rotated individual 'hooked' hair contours facing downwards to the left"

for filename in os.listdir(path):
    print(filename)
    img = cv2.imread(os.path.join(path,filename),0)
    #flip1 = cv2.flip(img, 0)
    flip2 = cv2.flip(img, 1)  ##right
    os.chdir(path3)
    cv2.imwrite(filename,flip2)
## 20XP down left ###

## 20XP up right ###
path6 = "path to the location of right-up folder i.e. extracted & rotated individual 'hooked' hair contours facing upwards to the right"

for filename in os.listdir(path):
    print(filename)
    img = cv2.imread(os.path.join(path,filename),0)
    flip1 = cv2.flip(img, 0) ## down
    #flip2 = cv2.flip(img, 1)
    os.chdir(path3)
    cv2.imwrite(filename,flip1)
## 20XP up right ###

## 20XP down right ###
path7 = "path to the location of right-down folder i.e. extracted & rotated individual 'hooked' hair contours facing downwards to the right"

for filename in os.listdir(path):
    img = cv2.imread(os.path.join(path,filename),0)
    print(filename)
    #flip1 = cv2.flip(img, 0)
    #flip2 = cv2.flip(img, 1)
    os.chdir(path3)
    cv2.imwrite(filename,img)
## 20XP down right ###