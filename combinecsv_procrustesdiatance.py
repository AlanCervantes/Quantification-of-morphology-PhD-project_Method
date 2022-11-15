# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 15:22:08 2022

@author: ar54482
"""

### This script was used to combine all *csv files into the final output csv file for procrustes distance ###

import os
import glob
import pandas as pd

path = "path to the location of output folder for procrustes distance i.e. csv file with the procrustes distance for each 'hooked' hair contour in the dataset"
path1 = "path to the location of output combined csv file with procrustes distance for the dataset"

os.chdir(path)
path=os.getcwd()
csv_files=glob.glob(os.path.join(path,"*.csv"))


##get all filenames
C=os.listdir()

##create an empty df
dfc=pd.DataFrame()

i=0
for f in csv_files:
    #print(f)
    df1=pd.read_csv(f)
    #df1['seed']=C[i]
    dfc=dfc.append(df1)
    i=i+1

print(dfc)

##get column list    
col=list(dfc.columns)
##save as csv file
dfc.to_csv(path1,index=False,header=True)
    
    
