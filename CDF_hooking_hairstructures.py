## Compare the degree of hooking in single cell plant structures by plotting CDF of the normalized deviation distances ##

## import libraries ##
from trichome_axis import disthistogramT
from hookedhair_axis import disthistogramH
from curledroothair_axis import disthistogramR
from sklearn import preprocessing
from trichome_axis import pltDataHist
from scipy.stats import norm
import cv2
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import ks_2samp


### get deviation for trichome ###
img_t=cv2.imread(r"/Users/ankita/Desktop/Data/Hooking_images/trichome_commonbean.png",0)
dis_t,skeletonCoordsX,skeletonCoordsY,choppedX,choppedY,fitX,fitY,x_new,y_new,Cx,Cy,orangePointY,orangePointX,mp=disthistogramT(img_t)


## get deviation for curled root hair ##
img_r=cv2.imread(r"/Users/ankita/Desktop/Data/Hooking_images/curledroothair_commonbean.png",0)
dis_r,skeletonCoordsX,skeletonCoordsY,choppedX,choppedY,fitX,fitY,Cx,Cy,x_new,y_new,orangePointX,orangePointY,Skelmidy,Skelmidy1=disthistogramR(img_r)


## get deviation for hooked hair ##
img_h=cv2.imread(r"/Users/ankita/Desktop/Data/Hooking_images/hookedhair_commonbean.png",0)
dis_h,skeletonCoordsX,skeletonCoordsY,choppedX,choppedY,fitX,fitY,x_new,y_new,Cx,Cy,orangePointY,orangePointX,Skelmidy,Skelmidy1=disthistogramH(img_h)

### make CDF ###

# drop the values where the axis overlaps with the medial axis #
##Trichome##
hist_list_input_int_droppedt = pltDataHist(dis_t)
## normalize the list ##
trichome_arr = preprocessing.normalize([np.array(hist_list_input_int_droppedt)])
muT, stdT = norm.fit(trichome_arr.reshape(-1,1))

##RootHair##
hist_list_input_int_droppedr = pltDataHist(dis_r)
## normalize the list ##
roothair_arr = preprocessing.normalize([np.array(hist_list_input_int_droppedr)])
muR, stdR = norm.fit(roothair_arr.reshape(-1,1))

# # ##HookedHair##
hist_list_input_int_droppedh = pltDataHist(dis_h)
## normalize the list ##
hookedhair_arr = preprocessing.normalize([np.array(hist_list_input_int_droppedh)])
muH, stdH = norm.fit(hookedhair_arr.reshape(-1,1))

# # Plot the CDF.
fig = plt.figure()
x = np.linspace(0, 1)
pT = norm.cdf(x, muT, stdT)
pR = norm.cdf(x, muR, stdR)
pH = norm.cdf(x, muH, stdH)
plt.plot(x, pT, 'k', linewidth=2, c='red', label='Trichome (T)')
plt.plot(x, pH, 'k', linewidth=2, c='green',label='Hooked Hair (H)')
plt.plot(x, pR, 'k', linewidth=2, c='blue',label='Curled Root Hair (R)')
plt.ylim((0,1.02))
plt.margins(0)
plt.legend(loc='lower right', frameon=False,framealpha=1,prop={'size': 8})
plt.show()

#### KS test #####
## Trichome-RH ##
print(ks_2samp(trichome_arr[0], roothair_arr[0]))

## HH-RH ##
print(ks_2samp(hookedhair_arr[0], roothair_arr[0]))

## Trichome-HH ##
print(ks_2samp(trichome_arr[0], hookedhair_arr[0]))


