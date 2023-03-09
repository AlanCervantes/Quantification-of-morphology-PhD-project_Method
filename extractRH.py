##Extract individual 'hooked' hair contours from segmented microscopic images##


#Import all libraries#
import cv2
import numpy as np
import os
import argparse
import sys


def ExtractRH(path1,path2):

    for filename in os.listdir(path1):

        print(filename) #print filename to check the code is running

        #Read the image you want the connected components from
        img = cv2.imread(os.path.join(path1,filename))

        #Make the image grayscale
        imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        #Get the dimensions of the image
        width, height = imgray.shape
        
        #Process every pixel to threshold the image
        for x in range(width):
            for y in range(height):
                p = imgray[x,y]
                if 50<p<100:
                    imgray[x,y]=255
                else:
                    imgray[x,y]=0     
        
        #Use the connected component labellling function of openCV
        ret, labels = cv2.connectedComponents(imgray,connectivity = 8)
        
        #Map component labels to hue val
        label_hue = np.uint8(179*labels/np.max(labels))
        blank_ch = 255*np.ones_like(label_hue)
        labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])
            
        #Cvt to BGR for display
        labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)
        
        #Set bg label to black
        labeled_img[label_hue==0] = 0
        
        l=0
        d=1 #initialize index for output files
        
        
        # Get the mask for each label
        for label in range(1,len(np.unique(labels))):
            mask = np.zeros_like(labels, dtype=np.uint8)
            mask[labels == label] = 255
            kernel = np.ones((5,5),np.uint8)
            mask=cv2.morphologyEx(mask, cv2.MORPH_OPEN,kernel)
            mask=cv2.morphologyEx(mask, cv2.MORPH_CLOSE,kernel)

            width, height = mask.shape ##collect only the white pixels i.e. the 'hooked' hairs
            for x in range(width):
                for y in range(height):
                    p = mask[x,y]
                    if p == 255:
                        l=l+1
        
            if l>0:

                outfile = '%d.png'%d #name each output file with individual contours
                d=d+1

                #save in the output folder
                os.chdir(path2) 

                filename=os.path.splitext(filename)[0]
                cv2.imwrite(filename+outfile, mask)
                print(filename+outfile)  #print output filename to check the code is running#

                os.chdir(path1)
                
            else:
                pass

            l=0
    return()


### Create command line interface (CLI) ###

##create the parser
parser = argparse.ArgumentParser(description='extract the contours of individual hooked hairs from the segmented images in path1 and save at path2')

## add arguments
parser.add_argument('path1', type=str, help='Data folder address')
parser.add_argument('path2', type=str, help='Output folder address')

## execute the parser
args = parser.parse_args()

#input for the command line#
path1=sys.argv[1]
path2=sys.argv[2]

#run the function#
ExtractRH(path1,path2)

#path examples#
#path1= (r"/Users/ankita/Desktop/DataAnalysis/RGB/Control_trial")
#path2= (r"/Users/ankita/Desktop/DataAnalysis/RGB")










