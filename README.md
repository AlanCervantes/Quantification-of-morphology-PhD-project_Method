# Quantification-of-morphology-PhD-project_Method

Code for the quantification of geometry (area & perimeter) and shape (procrustes distance) of single-cell plant structures and its analysis under nitrogen 
& phosphorus stress compared to the control.

## Installation

1. `git clone https://github.com/Ankita-30/Quantification-of-morphology-PhD-project_Method.git`
2. run `./build.sh` , 
   if permission is deined do $ `chmod 700 build.sh` 
   re-run $ `./build.sh`
3. To create the env run $ `source hookedHairQuantifucation/bin/activate'`
4. Install all dependent requrements by $ `pip install -r requirements.txt`

## Run

### Generation
1. To generate individual hooked hair run `python3 extractRH.py DataAnalysis/RGB/Control_trial DataAnalysis/RGB` **python3 extractRH.py input-path output-path Directory folders are local for example, input the data directory on your system**
 - **DataAnalysis/RGB/Control_trial**  is the input path with segmented microscopic images of hooked hairs
 - **DataAnalysis/RGB/Control_trial**  is the outout path where extracted individual hooked hairs are saved
 
### Quantification
2. To calculate area and perimeter of extracted hooked hair run `python3 Perimeter+CS.py DataAnalysis/RGB DataAnalysis/`, **'python3 Perimeter+CS.py input-path output-path' DataAnalysis/RGB should be the output directory from step 1**

### Analysis
4. To analyze how the area and perimeter changes under stress for each day (3,4,5) and growth category (low,mid,hogh) run `python3 Data_Analysis_AP.py Data_Files_Morphology/DataCellShapeC_pipeline.csv Data_Files_Morphology/DataCellShapeNS_pipeline.csv Data_Files_Morphology/DataCellShapePS_pipeline.csv output-path` **'python3 Data_Analysis_AP.py input-path1 input-path2 input-path3 output-path' input paths 1,2 & 3 are the output paths from step 2 for 3 treatment conditions (Control(C), P-stress(PS) & N-stress(NS)) in our experiment output-path is the location to store the output csv file**

5. To analyze how length changes under stress for each day (3,4,5) and growth category (low,mid,high) run `python3 Data_Analysis_Length.py Data_Files_Morphology/Data_cellshapeC_length.csv Data_Files_Morphology/Data_cellshapePS_length.csv Data_Files_Morphology/Data_cellshapeNS_length.csv output-path`**'python3 Data_Analysis_Length.py input-path1 input-path2 input-path3 output-path' input paths 1,2 & 3 are the output paths from step 2 for 3 treatment conditions (Control(C), P-stress(PS) & N-stress(NS)) in our experiment output-path is the location to store the output csv file**

6. To analyze how shape changes under stress for each day (3,4,5) and growth category (low,mid,high)run `python3 Data_Analysis_Shape_PD.py Data_Files_Morphology/Data_cellshape_Control.csv Data_Files_Morphology/Data_cellshape_PStress.csv Data_Files_Morphology/Data_cellshape_NStress.csv output-path`**'python3 Data_Analysis_Length.py input-path1 input-path2 input-path3 output-path' input paths 1,2 & 3 are the output paths from step 2 for 3 treatment conditions (Control(C), P-stress(PS) & N-stress(NS)) in our experiment output-path is the location to store the output csv file**
`

