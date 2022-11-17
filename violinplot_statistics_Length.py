#Import all libraries
import pandas as pd
from scipy import stats


path1=r"Data_Files_Morphology/Data_cellshapeC_length.csv"
path2=r"Data_Files_Morphology/Data_cellshapePS_length.csv"
path3=r"Data_Files_Morphology/Data_cellshapeNS_length.csv"


def Data_Analysis(path1,path2,path3):

    # #create an empty df
    dfc=pd.DataFrame()
    #read the csv file
    dfc=pd.read_csv(path1)
    #print(dfc)

    # #N-stress
    # #create an empty df
    dfn=pd.DataFrame()
    #read the csv file
    dfn=pd.read_csv(path3)
    #print(dfn)

    # #P-stress
    #create an empty df
    dfp=pd.DataFrame()
    #read the csv file
    dfp=pd.read_csv(path2)
    #print(dfp)



    ####CONTROL###

    print("Control")

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
        df1=(dfc[dfc['Control'].str.match(x)])
        df3c=df3c.append(df1)

    for x in day4:
        df1=(dfc[dfc['Control'].str.match(x)])
        df4c=df4c.append(df1)

    for x in day5:
        df1=(dfc[dfc['Control'].str.match(x)])
        df5c=df5c.append(df1)

        ###Parse df by root length low, mid and high###
    #list according to root growth
    l=["sd1_","sd2_","sd4_","sd6_","sd7_","sd11_","sd21_","sd28_","sd3_"]
    m=["sd8_","sd9_","sd10_","sd12_","sd14_","sd16_","sd17_","sd20_","sd22_","sd23_","sd25_","sd26_"]
    h=["sd13_","sd15_","sd18_","sd19_","sd24_","sd27_"]


    #select rows according to the root length
    for x in l:
        df1=(dfc[dfc['Control'].str.match(x)])
        dflc=dflc.append(df1)

    for x in m:
        df1=(dfc[dfc['Control'].str.match(x)])
        dfmc=dfmc.append(df1)

    for x in h:
        df1=(dfc[dfc['Control'].str.match(x)])
        dfhc=dfhc.append(df1)

    # ###PSTRESS###

    print('PStress')

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
        df1=(dfp[dfp['seed'].str.match(x)])
        df3p=df3p.append(df1)

    for x in day4:
        df1=(dfp[dfp['seed'].str.match(x)])
        df4p=df4p.append(df1)

    for x in day5:
        df1=(dfp[dfp['seed'].str.match(x)])
        df5p=df5p.append(df1)

    ##Parse df by root length low, mid and high###
    #list according to root growth
    l=["sd1_","sd2_","sd10_","sd13_","sd14_","sd17_","sd22_","sd11_","sd28_","sd29_"]
    m=["sd4_","sd5_","sd8_","sd9_","sd18_","sd19_","sd20_","sd23_","sd12_","sd27_","sd30_"]
    h=["sd3_","sd6_","sd7_","sd15_","sd16_","sd21_","sd26_"]

    #add last 6 seeds###

    #select rows according to the root length
    for x in l:
        df1=(dfp[dfp['seed'].str.match(x)])
        dflp=dflp.append(df1)

    for x in m:
        df1=(dfp[dfp['seed'].str.match(x)])
        dfmp=dfmp.append(df1)

    for x in h:
        df1=(dfp[dfp['seed'].str.match(x)])
        dfhp=dfhp.append(df1)
        
    # ###NSTRESS###

    print('NStress')

    # ###Parse df by Days 3,4 & 5###
    # #list according to root age
    day3=["sd2_","sd3_","sd4_","sd15_","sd16_","sd17_","sd22_","sd23_","sd24_"]
    day4=["sd1_","sd7_","sd8_","sd9_","sd10_","sd11_","sd12_","sd13_","sd18_","sd19_","sd20_","sd21_","sd25_","sd26_"]
    day5=["sd5_","sd6_","sd14_","sd27_","sd28_","sd29_","sd30_"]

    # #create six empty dfs
    df3n=pd.DataFrame()
    df4n=pd.DataFrame()
    df5n=pd.DataFrame()
    dfln=pd.DataFrame()
    dfmn=pd.DataFrame()
    dfhn=pd.DataFrame()

    # print(dfn)

    # #select rows according to the root age
    for x in day3:
        df1=(dfn[dfn['seed'].str.match(x)])
        df3n=df3n.append(df1)

    for x in day4:
        df1=(dfn[dfn['seed'].str.match(x)])
        df4n=df4n.append(df1)

    for x in day5:
        df1=(dfn[dfn['seed'].str.match(x)])
        df5n=df5n.append(df1)

    # ##Parse df by root length low, mid and high###
    #list according to root growth
    l=["sd3_","sd2_","sd4_","sd5_","sd25_","sd22_","sd24_","sd27_","sd19_"]
    m=["sd8_","sd7_","sd6_","sd12_","sd16_","sd17_","sd23_","sd21_","sd26_","sd30_"]
    h=["sd1_","sd9_","sd10_","sd11_","sd13_","sd14_","sd15_","sd18_","sd28_","sd29_","sd20_"]

    #select rows according to the root length
    for x in l:
        df1=(dfn[dfn['seed'].str.match(x)])
        dfln=dfln.append(df1)

    for x in m:
        df1=(dfn[dfn['seed'].str.match(x)])
        dfmn=dfmn.append(df1)

    for x in h:
        df1=(dfn[dfn['seed'].str.match(x)])
        dfhn=dfhn.append(df1)

    return(df3c,df4c,df5c,dflc,dfmc,dfhc,df3n,df4n,df5n,dfln,dfmn,dfhn,df3p,df4p,df5p,dflp,dfmp,dfhp)

df3c,df4c,df5c,dflc,dfmc,dfhc,df3n,df4n,df5n,dfln,dfmn,dfhn,df3p,df4p,df5p,dflp,dfmp,dfhp=Data_Analysis(path1,path2,path3)


##Control##
#Area#
C3a=df3c['length_mu'].to_list()
print('C3',stats.describe(C3a))
C4a=df4c['length_mu'].to_list()
print('C4',stats.describe(C4a))
C5a=df5c['length_mu'].to_list()
print('C5',stats.describe(C5a))
Cla=dflc['length_mu'].to_list()
print('Cl',stats.describe(Cla))
Cma=dfmc['length_mu'].to_list()
print('Cm',stats.describe(Cma))
Cha=dfhc['length_mu'].to_list()
print('Ch',stats.describe(Cha))

#P-Stress#
P3a=df3p['length_mu'].to_list()
print('3',stats.describe(P3a))
P4a=df4p['length_mu'].to_list()
print('4',stats.describe(P4a))
P5a=df5p['length_mu'].to_list()
print('5',stats.describe(P5a))
Pla=dflp['length_mu'].to_list()
print('l',stats.describe(Pla))
Pma=dfmp['length_mu'].to_list()
print('m',stats.describe(Pma))
Pha=dfhp['length_mu'].to_list()
print('h',stats.describe(Pha))

#N-Stress#
P3a=df3n['length_mu'].to_list()
print('N3',stats.describe(P3a))
P4a=df4n['length_mu'].to_list()
print('N4',stats.describe(P4a))
P5a=df5n['length_mu'].to_list()
print('N5',stats.describe(P5a))
Pla=dfln['length_mu'].to_list()
print('Nl',stats.describe(Pla))
Pma=dfmn['length_mu'].to_list()
print('Nm',stats.describe(Pma))
Pha=dfhn['length_mu'].to_list()
print('Nh',stats.describe(Pha))
