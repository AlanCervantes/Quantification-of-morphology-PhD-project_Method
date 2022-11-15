# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 16:24:06 2021

@author: ar54482
"""
### This script was used for ICP implementation and calculation of procrustes distance to quantify the shape of 'hooked' hairs ###

import json
import os
import ICP
import matplotlib.pyplot as plt
import cv2
import numpy as np
import math
from scipy.spatial import distance
import pandas as pd


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

def mindistpq(p,C2):

    #min=math.sqrt(sum([(a - b) ** 2 for a, b in zip(p, C2[0])]))
    min=distance.euclidean(p,C2[0])

    for y in C2:
        dist=distance.euclidean(p,y)
        #distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(p, y)]))
        if dist<min:
            min=dist

    return(min)    
    
#superimpose all shapes to an average shape

#### ICP ###############
Data=[]
procrustes=[]
PDist=[]
Filename=[]

path = "path to the location of final pre-aligned folder i.e. oriented individual 'hooked' hair contours ready for ICP implementation"
path1 = "path to the location of superimposed folder i.e. oriented individual 'hooked' hair contours superimposed to the model image"
path2 = "path to the location of output folder for procrustes distance i.e. csv file with the procrustes distance for each 'hooked' hair contour in the dataset"
path3 = "path to the location of file of data contour coordinates in ICP implementation"
path4 = "path to the location of file of model contour coordinates in ICP implementation"
path5 = "path to the location of file of superimposed data coordinates in ICP implementation"

for filename in os.listdir(path):
    
    print(filename)
    Filename.append(filename)
    
    icp = ICP.ICP(
                binary_or_color = "color",
                corners_or_edges = "edges",
                auto_select_model_and_data = 1,
                calculation_image_size = 200,
                max_num_of_pixels_used_for_icp = 450,
                pixel_correspondence_dist_threshold = 4000,
                iterations = 15,
                model_image =  "model.png",
                data_image = filename,
                font_file="/usr/share/fonts/truetype/freefont/FreeSerf.ttf"
              )
    
    icp.extract_pixels_from_color_image("model")
    icp.extract_pixels_from_color_image("data")
    icp.icp()
    icp.cleanup_directory()


    with open(path3) as f:
        data_coords= json.load(f)
        Data.append(data_coords)
    
    with open(path4) as f:
        model_coords= json.load(f)
        
    with open(path5) as f:
        procrustes_coords= json.load(f)
        procrustes.append(procrustes_coords)
    
    
    #model shape
    C1=model_coords
    
    ##plot superimposed image##
 
    #plt.figure(1) 
    fig,ax=plt.subplots(1,1)
    ax=plt.scatter(GetXfromI(procrustes_coords),GetYfromI(procrustes_coords))
    os.chdir(path1)
    plt.savefig(filename)
    os.chdir(path)
    plt.show()
    
    
    ##calculate procrustes distance (PD)
    C2=procrustes_coords

    #first term of PD
    Min_listC1=[]
    for x in C1:
        d=mindistpq(x,C2)
        Min_listC1.append(d*d)
    
    ## find sum of list 
    sumC1=sum(Min_listC1)
    
    ##second term of PD
    Min_listC2=[]

    for x in C2:
        d=mindistpq(x,C1)
        Min_listC2.append(d*d)
    
    ## find list of minimum distance (p->q) for all p
    
    ## find sum of list 
    sumC2=sum(Min_listC2)
    
    ##find procrustes metric 
    PD=np.sqrt(0.5*((1/len(C1))*sumC1 + (1/len(C2))*sumC2))
    print(PD)
    PDist.append(PD)

    data={'ID':[filename],'Pdist':[PD]}

    NS=pd.DataFrame(data)
    os.chdir(path2)
    filename=os.path.splitext(filename)[0]
    NS.to_csv(filename + '.csv',index=False,header=True)
    os.chdir(path)
    NS.drop(NS.index,inplace=True) 
    
#### ICP ###############
