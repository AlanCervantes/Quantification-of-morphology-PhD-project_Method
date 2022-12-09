import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn import decomposition
import matplotlib.pyplot as plt
import matplotlib


## All functions here ##
def PCA_Dataset_Prep(xl_1,xl_2,xl_3,k,m):
    PCA_P= xl_1.parse(m)

    ## modify filename column ##
    PS=list(PCA_P[k])
    PS_mod=[]

    for l in PS:
        l=l.rsplit( ".", 1 )[ 0 ]
        PS_mod.append(l)
        
    PCA_P[k]=PS_mod
    P_length= xl_2.parse('Sheet1')

    ## modify filename column ##
    PS=list(P_length[k])
    PS_mod=[]

    for l in PS:
        l=l.rsplit( "_", 1 )[ 0 ]
        PS_mod.append(l)
        
    P_length[k]=PS_mod

    ## merge two dataframes ##
    PCA_Pl=pd.merge(P_length,PCA_P,on=k)
    P_shape= xl_3.parse('Sheet1')
    
    ## modify filename column ##
    PS=list(P_shape[k])
    PS_mod=[]

    for l in PS:
        l=l.rsplit( ".", 1 )[ 0 ]
        PS_mod.append(l)
        
    P_shape[k]=PS_mod
    
    ## merge two dataframes ##
    PCA_Pls=pd.merge(P_shape,PCA_Pl,on=k)
    PCA_Pls.rename(columns = {k:'seed'}, inplace = True)
    return(PCA_Pls)


## All functions here ##

## Load all datasets ##

#P-stress#
xl_1p = pd.ExcelFile(r"/Users/ankita/Desktop/DataAnalysis/RGB/Procrustes/Re-analysis/Peter_Reanalysis/Procrustes_averageshape_calculation.xlsx")
## Add the length values ##
xl_2p = pd.ExcelFile(r"/Users/ankita/Desktop/DataAnalysis/RGB/Procrustes/Re-analysis/Peter_Reanalysis/Data_cellshapePS_length.xlsx")
## Add the shape values ##
xl_3p = pd.ExcelFile(r"/Users/ankita/Desktop/DataAnalysis/RGB/Procrustes/Re-analysis/Peter_Reanalysis/Procrustes_outlier/Procrustes_outlier_redo/Data_cellshape_PStress.xlsx")

#N-stress#
xl_1n = pd.ExcelFile(r"/Users/ankita/Desktop/DataAnalysis/RGB/Procrustes/Re-analysis/Peter_Reanalysis/Procrustes_averageshape_calculation.xlsx")
## Add the length values ##
xl_2n = pd.ExcelFile(r"/Users/ankita/Desktop/DataAnalysis/RGB/Procrustes/Re-analysis/Peter_Reanalysis/Data_cellshapeNS_length.xlsx")
## Add the shape values ##
xl_3n = pd.ExcelFile(r"/Users/ankita/Desktop/DataAnalysis/RGB/Procrustes/Re-analysis/Peter_Reanalysis/Procrustes_outlier/Procrustes_outlier_redo/Data_cellshape_NStress.xlsx")

#Control#
xl_1c = pd.ExcelFile(r"/Users/ankita/Desktop/DataAnalysis/RGB/Procrustes/Re-analysis/Peter_Reanalysis/Procrustes_averageshape_calculation.xlsx")
## Add the length values ##
xl_2c = pd.ExcelFile(r"/Users/ankita/Desktop/DataAnalysis/RGB/Procrustes/Re-analysis/Peter_Reanalysis/Data_cellshapeC_length.xlsx")
## Add the shape values ##
xl_3c = pd.ExcelFile(r"/Users/ankita/Desktop/DataAnalysis/RGB/Procrustes/Re-analysis/Peter_Reanalysis/Procrustes_outlier/Procrustes_outlier_redo/Data_cellshape_Control.xlsx")

## Load all datasets ##

## Prepare dataset for PCA Analysis ##

PCA_N=PCA_Dataset_Prep(xl_1n,xl_2n,xl_3n,'Nstress','PCA_N')
PCA_N=PCA_N.assign(Group=1)
PCA_N.drop('seed', axis=1, inplace=True)


PCA_C=PCA_Dataset_Prep(xl_1c,xl_2c,xl_3c,'Control','PCA_C')
PCA_C=PCA_C.assign(Group=2)
PCA_C.drop('seed', axis=1, inplace=True)


PCA_P=PCA_Dataset_Prep(xl_1p,xl_2p,xl_3p,'Pstress','PCA_P')
PCA_P=PCA_P.assign(Group=3)
PCA_P.drop('seed', axis=1, inplace=True)


## Prepare dataset for PCA Analysis ##


## PCA ##

## combined datatframe ##
PCA=pd.concat([PCA_N, PCA_C, PCA_P], axis=0)

## scale the data ##
features=PCA.columns[:-1]
x = PCA.loc[:, features].values
x = StandardScaler().fit_transform(x)

## label ##
label=PCA.columns[-1]
y = PCA.loc[:, label].values
label = [1,2,3]
colors = ['green','blue','red']


##PCA##
pca = decomposition.PCA(n_components=3)
principalComponents = pca.fit_transform(x)
principal_Df = pd.DataFrame(data = principalComponents, columns = ['principal component 1', 'principal component 2','principal component 3'])
print(principal_Df)
print(pca.explained_variance_)


## plot PCA ##
## set  3D axis ##
fig = plt.figure(1, figsize=(4, 3))
plt.clf()

ax = fig.add_subplot(111, projection="3d", elev=48, azim=134)
ax.set_position([0, 0, 0.95, 1])
plt.cla()

ax.scatter(principalComponents[:, 0], principalComponents[:, 1], principalComponents[:, 2], c=y, cmap=matplotlib.colors.ListedColormap(colors))

ax.w_xaxis.set_ticklabels([])
ax.w_yaxis.set_ticklabels([])
ax.w_zaxis.set_ticklabels([])

ax.set_xlabel('PC 1')
ax.set_ylabel('PC 2')
ax.set_zlabel('PC 3')

plt.show()










