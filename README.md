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
4. To analyze how the area and perimeter changes under stress for each day (3,4,5) and growth category (low,mid,hogh) run `python3 Data_Analysis_AP.py Data_Files_Morphology/DataCellShapeC_pipeline.csv Data_Files_Morphology/DataCellShapePS_pipeline.csv Data_Files_Morphology/DataCellShapeNS_pipeline.csv` **'python3 Data_Analysis_AP.py input-path' the input path is the output path from step 2**
5. To analyze how the area and perimeter changes under stress for each day (3,4,5) and growth category (low,mid,hogh) run `python3 Data_Analysis_AP.py Data_Files_Morphology/DataCellShapeC_pipeline.csv Data_Files_Morphology/DataCellShapePS_pipeline.csv Data_Files_Morphology/DataCellShapeNS_pipeline.csv`

