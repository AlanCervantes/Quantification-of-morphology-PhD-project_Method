
## Code to calculate the mean, variance, skewness and kurtosis of data for area and perimeter for each day and growth category ##

## import libraries ##
import pandas as pd
from scipy import stats
import numpy as np


# All functions here ####

path1=r"/Users/ankita/Desktop/DataAnalysis/RGB/Procrustes/Re-analysis/Peter_Reanalysis/DataCellShapeC_pipeline.csv"
path2=r"/Users/ankita/Desktop/DataAnalysis/RGB/Procrustes/Re-analysis/Peter_Reanalysis/DataCellShapeNS_pipeline.csv"
path3=r"/Users/ankita/Desktop/DataAnalysis/RGB/Procrustes/Re-analysis/Peter_Reanalysis/DataCellShapePS_pipeline.csv"



def Data_Analysis(path1, path2, path3):
    
    #Control
    # print('Control')

    #create an empty df
    dfc=pd.DataFrame()
    #read the csv file
    dfc=pd.read_csv(path1)

    #N-stress
    #create an empty df
    dfn=pd.DataFrame()
    #read the csv file
    dfn=pd.read_csv(path2)

    #P-stress
    #create an empty df
    dfp=pd.DataFrame()
    #read the csv file
    dfp=pd.read_csv(path3)

    ###CONTROL###
    ###Parse df by Days 3,4 & 5###
    #list according to root age
    day3=["sd1_","sd2_","sd3_","sd14_","sd15_","sd17_","sd18_","sd19_","sd20_","sd21_","sd22_","sd23_","sd24_","sd25_" ]
    day4=["sd4_","sd5_","sd6_","sd7_","sd8_","sd16_","sd26_","sd27_","sd28_","sd9_"]
    day5=["sd10_","sd11_","sd12_"]

    #create six empty dfs
    df3c=pd.DataFrame()
    df4c=pd.DataFrame()
    df5c=pd.DataFrame()
    dflc=pd.DataFrame()
    dfmc=pd.DataFrame()
    dfhc=pd.DataFrame()

    #select rows according to the root age
    for x in day3:
        df1=(dfc[dfc['ID'].str.match(x)])
        df3c=df3c.append(df1)

    for x in day4:
        df1=(dfc[dfc['ID'].str.match(x)])
        df4c=df4c.append(df1)

    for x in day5:
        df1=(dfc[dfc['ID'].str.match(x)])
        df5c=df5c.append(df1)


    ###Parse df by root length low, mid and high###
    #list according to root growth
    l=["sd1_","sd2_","sd4_","sd6_","sd7_","sd11_","sd21_","sd28_","sd3_"]
    m=["sd8_","sd9_","sd10_","sd12_","sd14_","sd16_","sd17_","sd20_","sd22_","sd23_","sd25_","sd26_"]
    h=["sd13_","sd15_","sd18_","sd19_","sd24_","sd27_"]


    #select rows according to the root length
    for x in l:
        df1=(dfc[dfc['ID'].str.match(x)])
        dflc=dflc.append(df1)

    for x in m:
        df1=(dfc[dfc['ID'].str.match(x)])
        dfmc=dfmc.append(df1)

    for x in h:
        df1=(dfc[dfc['ID'].str.match(x)])
        dfhc=dfhc.append(df1)


    ###PSTRESS###

    # print('PStress')

    ###Parse df by Days 3,4 & 5###
    #list according to root age
    day3=["sd3_","sd4_","sd5_","sd6_","sd7_","sd8_","sd9_"]
    day4=["sd1_","sd2_","sd10_","sd11_","sd12_","sd13_","sd14_","sd22_","sd23_","sd28_","sd29_","sd30_"]
    day5=["sd15_","sd16_","sd17_","sd18_","sd19_","sd20_","sd21_","sd26_","sd27_"]

    #create six empty dfs
    df3p=pd.DataFrame()
    df4p=pd.DataFrame()
    df5p=pd.DataFrame()
    dflp=pd.DataFrame()
    dfmp=pd.DataFrame()
    dfhp=pd.DataFrame()

    #select rows according to the root age
    for x in day3:
        df1=(dfp[dfp['ID'].str.match(x)])
        df3p=df3p.append(df1)

    for x in day4:
        df1=(dfp[dfp['ID'].str.match(x)])
        df4p=df4p.append(df1)

    for x in day5:
        df1=(dfp[dfp['ID'].str.match(x)])
        df5p=df5p.append(df1)
    

    ###Parse df by root length low, mid and high###
    #list according to root growth
    l=["sd1_","sd2_","sd10_","sd13_","sd14_","sd17_","sd22_","sd11_","sd28_","sd29_"]
    m=["sd4_","sd5_","sd8_","sd9_","sd18_","sd19_","sd20_","sd23_","sd12_","sd27_","sd30_"]
    h=["sd3_","sd6_","sd7_","sd15_","sd16_","sd21_","sd26_"]

    #select rows according to the root length
    for x in l:
        df1=(dfp[dfp['ID'].str.match(x)])
        dflp=dflp.append(df1)

    for x in m:
        df1=(dfp[dfp['ID'].str.match(x)])
        dfmp=dfmp.append(df1)

    for x in h:
        df1=(dfp[dfp['ID'].str.match(x)])
        dfhp=dfhp.append(df1)

    ###NSTRESS###

    # print('NStress')

    ###Parse df by Days 3,4 & 5###
    #list according to root age
    day3=["sd2_","sd3_","sd4_","sd15_","sd16_","sd17_","sd22_","sd23_","sd24_"]
    day4=["sd1_","sd7_","sd8_","sd9_","sd10_","sd11_","sd12_","sd13_","sd18_","sd19_","sd20_","sd21_","sd25_","sd26_"]
    day5=["sd5_","sd6_","sd14_","sd27_","sd28_","sd29_","sd30_"]

    #create six empty dfs
    df3n=pd.DataFrame()
    df4n=pd.DataFrame()
    df5n=pd.DataFrame()
    dfln=pd.DataFrame()
    dfmn=pd.DataFrame()
    dfhn=pd.DataFrame()

    #select rows according to the root age
    for x in day3:
        df1=(dfn[dfn['ID'].str.match(x)])
        df3n=df3n.append(df1)

    for x in day4:
        df1=(dfn[dfn['ID'].str.match(x)])
        df4n=df4n.append(df1)

    for x in day5:
        df1=(dfn[dfn['ID'].str.match(x)])
        df5n=df5n.append(df1)
    

    ###Parse df by root length low, mid and high###
    #list according to root growth
    l=["sd3_","sd2_","sd4_","sd5_","sd25_","sd22_","sd24_","sd27_","sd19_"]
    m=["sd8_","sd7_","sd6_","sd12_","sd16_","sd17_","sd23_","sd21_","sd26_","sd30_"]
    h=["sd1_","sd9_","sd10_","sd11_","sd13_","sd14_","sd15_","sd18_","sd28_","sd29_","sd20_"]

    #select rows according to the root length
    for x in l:
        df1=(dfn[dfn['ID'].str.match(x)])
        dfln=dfln.append(df1)

    for x in m:
        df1=(dfn[dfn['ID'].str.match(x)])
        dfmn=dfmn.append(df1)

    for x in h:
        df1=(dfn[dfn['ID'].str.match(x)])
        dfhn=dfhn.append(df1)

    return(df3c,df4c,df5c,dflc,dfmc,dfhc,df3n,df4n,df5n,dfln,dfmn,dfhn,df3p,df4p,df5p,dflp,dfmp,dfhp)

df3c,df4c,df5c,dflc,dfmc,dfhc,df3n,df4n,df5n,dfln,dfmn,dfhn,df3p,df4p,df5p,dflp,dfmp,dfhp=Data_Analysis(path1,path2,path3)

##Control##
#Area#
C3a=df3c['Area'].to_list()
print('C3',stats.describe(C3a))
C4a=df4c['Area'].to_list()
print('C4',stats.describe(C4a))
C5a=df5c['Area'].to_list()
print('C5',stats.describe(C5a))
Cla=dflc['Area'].to_list()
print('Cl',stats.describe(Cla))
Cma=dfmc['Area'].to_list()
print('Cm',stats.describe(Cma))
Cha=dfhc['Area'].to_list()
print('Ch',stats.describe(Cha))

# #Perimeter#
C3p=df3c['Perimeter'].to_list()
print('C3',stats.describe(C3p))
C4p=df4c['Perimeter'].to_list()
print('C4',stats.describe(C4p))
C5p=df5c['Perimeter'].to_list()
print('C4',stats.describe(C5p))
Clp=dflc['Perimeter'].to_list()
print('C4',stats.describe(Clp))
Cmp=dfmc['Perimeter'].to_list()
print('C4',stats.describe(Cmp))
Chp=dfhc['Perimeter'].to_list()
print('C4',stats.describe(Chp))

##P-Stress##
#Area#
P3a=df3p['Area'].to_list()
print('3',stats.describe(P3a))
P4a=df4p['Area'].to_list()
print('4',stats.describe(P4a))
P5a=df5p['Area'].to_list()
print('5',stats.describe(P5a))
Pla=dflp['Area'].to_list()
print('l',stats.describe(Pla))
Pma=dfmp['Area'].to_list()
print('m',stats.describe(Pma))
Pha=dfhp['Area'].to_list()
print('h',stats.describe(Pha))

#Perimeter#
P3p=df3p['Perimeter'].to_list()
print('3',stats.describe(P3p))
P4p=df4p['Perimeter'].to_list()
print('4',stats.describe(P4p))
P5p=df5p['Perimeter'].to_list()
print('4',stats.describe(P5p))
Plp=dflp['Perimeter'].to_list()
print('4',stats.describe(Plp))
Pmp=dfmp['Perimeter'].to_list()
print('4',stats.describe(Pmp))
Php=dfhp['Perimeter'].to_list()
print('4',stats.describe(Php))

##N-Stress##
#Area#
P3a=df3n['Area'].to_list()
print('N3',stats.describe(P3a))
P4a=df4n['Area'].to_list()
print('N4',stats.describe(P4a))
P5a=df5n['Area'].to_list()
print('N5',stats.describe(P5a))
Pla=dfln['Area'].to_list()
print('Nl',stats.describe(Pla))
Pma=dfmn['Area'].to_list()
print('Nm',stats.describe(Pma))
Pha=dfhn['Area'].to_list()
print('Nh',stats.describe(Pha))

# #Perimeter#
N3p=df3n['Perimeter'].to_list()
print('C3',stats.describe(N3p))
N4p=df4n['Perimeter'].to_list()
print('C4',stats.describe(N4p))
N5p=df5n['Perimeter'].to_list()
print('C4',stats.describe(N5p))
Nlp=dfln['Perimeter'].to_list()
print('C4',stats.describe(Nlp))
Nmp=dfmn['Perimeter'].to_list()
print('C4',stats.describe(Nmp))
Nhp=dfhn['Perimeter'].to_list()
print('C4',stats.describe(Nhp))


