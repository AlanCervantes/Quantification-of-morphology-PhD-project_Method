
### new analyisis of length by Peter - 2022 #####

#Import all libraries
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import math
import random
import statistics
from scipy.stats import ttest_ind
import numpy as np
import seaborn as sb

path1=r"Data_Files_Morphology/Data_cellshape_Control.csv"
path2=r"Data_Files_Morphology/Data_cellshape_PStress.csv"
path3=r"Data_Files_Morphology/Data_cellshape_NStress.csv"
path4=r"Data_Files_Morphology/Data_Compile_shape_outlier.xlsx"

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

print(dfc)

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
    df1=(dfc[dfc['seed'].str.match(x)])
    df3c=df3c.append(df1)

for x in day4:
    df1=(dfc[dfc['seed'].str.match(x)])
    df4c=df4c.append(df1)

for x in day5:
    df1=(dfc[dfc['seed'].str.match(x)])
    df5c=df5c.append(df1)

print(len(df3c)+len(df4c)+len(df5c)) 

    ###Parse df by root length low, mid and high###
#list according to root growth
l=["sd1_","sd2_","sd4_","sd6_","sd7_","sd11_","sd21_","sd28_","sd3_"]
m=["sd8_","sd9_","sd10_","sd12_","sd14_","sd16_","sd17_","sd20_","sd22_","sd23_","sd25_","sd26_"]
h=["sd13_","sd15_","sd18_","sd19_","sd24_","sd27_"]


#select rows according to the root length
for x in l:
    df1=(dfc[dfc['seed'].str.match(x)])
    dflc=dflc.append(df1)

for x in m:
    df1=(dfc[dfc['seed'].str.match(x)])
    dfmc=dfmc.append(df1)

for x in h:
    df1=(dfc[dfc['seed'].str.match(x)])
    dfhc=dfhc.append(df1)

print(len(dflc)+len(dfmc)+len(dfhc)) 

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
    
print(len(df3p)+len(df4p)+len(df5p))  

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
    
print(len(dflp)+len(dfmp)+len(dfhp))    
# print(dfp)

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
    
print(len(df3n)+len(df4n)+len(df5n))  

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
    
print(len(dfln)+len(dfmn)+len(dfhn)) 

#day3
headers = ['PD_c','PD_p','PD_n']
data=[list(df3c["Pdist"]),list(df3p["Pdist"]),list(df3n["Pdist"])]
dict3 = {headers[0]:data[0],headers[1]:data[1],headers[2]:data[2]}
day3=pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in dict3.items()]))

#day4
headers = ['PD_c','PD_p','PD_n']
data=[list(df4c["Pdist"]),list(df4p["Pdist"]),list(df4n["Pdist"])]
dict3 = {headers[0]:data[0],headers[1]:data[1],headers[2]:data[2]}
day4=pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in dict3.items()]))

#day5
headers = ['PD_c','PD_p','PD_n']
data=[list(df5c["Pdist"]),list(df5p["Pdist"]),list(df5n["Pdist"])]
dict3 = {headers[0]:data[0],headers[1]:data[1],headers[2]:data[2]}
day5=pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in dict3.items()]))

##Low
headers = ['PD_c','PD_p','PD_n']
data=[list(dflc["Pdist"]),list(dflp["Pdist"]),list(dfln["Pdist"])]
dictl = {headers[0]:data[0],headers[1]:data[1],headers[2]:data[2]}
dayl=pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in dictl.items()]))

##Mid
headers = ['PD_c','PD_p','PD_n']
data=[list(dfmc["Pdist"]),list(dfmp["Pdist"]),list(dfmn["Pdist"])]
dictl = {headers[0]:data[0],headers[1]:data[1],headers[2]:data[2]}
daym=pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in dictl.items() ]))

##High
headers = ['PD_c','PD_p','PD_n']
data=[list(dfhc["Pdist"]),list(dfhp["Pdist"]),list(dfhn["Pdist"])]
dictl = {headers[0]:data[0],headers[1]:data[1],headers[2]:data[2]}
dayh=pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in dictl.items() ]))


# ####Parse df into Stress###
# #CONTROL#
headers = ['PD_3','PD_4','PD_5','PD_l','PD_m','PD_h']
data=[list(df3c["Pdist"]),list(df4c["Pdist"]),list(df5c["Pdist"]),list(dflc["Pdist"]),list(dfmc["Pdist"]),list(dfhc["Pdist"])]
dictcontrol = {headers[0]:data[0],headers[1]:data[1],headers[2]:data[2],headers[3]:data[3],headers[4]:data[4],headers[5]:data[5]}
control=pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in dictcontrol.items() ]))

##PStress#
headers = ['PD_3','PD_4','PD_5','PD_l','PD_m','PD_h']
data=[list(df3p["Pdist"]),list(df4p["Pdist"]),list(df5p["Pdist"]),list(dflp["Pdist"]),list(dfmp["Pdist"]),list(dfhp["Pdist"])]
dictpstress = {headers[0]:data[0],headers[1]:data[1],headers[2]:data[2],headers[3]:data[3],headers[4]:data[4],headers[5]:data[5]}
pstress=pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in dictpstress.items() ]))

##NStress#
headers = ['PD_3','PD_4','PD_5','PD_l','PD_m','PD_h']
data=[list(df3n["Pdist"]),list(df4n["Pdist"]),list(df5n["Pdist"]),list(dfln["Pdist"]),list(dfmn["Pdist"]),list(dfhn["Pdist"])]
dictnstress = {headers[0]:data[0],headers[1]:data[1],headers[2]:data[2],headers[3]:data[3],headers[4]:data[4],headers[5]:data[5]}
nstress=pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in dictnstress.items() ]))



# ###Combine df to form the cumulative df###
headers = ['PD_c','PD_p','PD_n']
data=[list(dfc["Pdist"]),list(dfp["Pdist"]),list(dfn["Pdist"])]
dict3 = {headers[0]:data[0],headers[1]:data[1],headers[2]:data[2]}
Cumulative=pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in dict3.items() ]))

# ##final spreadsheet ##
dflist1=[day3,day4,day5,dayl,daym,dayh,control,pstress,nstress,Cumulative]

Excelwriter = pd.ExcelWriter(path4,engine="xlsxwriter")
for df in dflist1:
    namestr= [name for name in globals() if globals()[name] is df]
    #print(namestr)
    df.to_excel(Excelwriter,sheet_name=namestr[0], index=False)

Excelwriter.save()

#visualize data

#make box_plot for area##

xl = pd.ExcelFile(path4)

df = xl.parse('Cumulative')
Col=list(df.columns)

C=df['PD_c']
Cl = df[Col[0]].values

N=df['PD_n']
Nl = df[Col[2]].values

P=df['PD_p']
Pl = df[Col[1]].values

my_colors=['blue','green','red']

df1=pd.DataFrame({'P-Stress':P,'Control':C,'N-Stress':N})
ax=df1.boxplot(grid=False,patch_artist = True,color='black')

#put color according to stress
ax.findobj(matplotlib.patches.Patch)[0].set_facecolor("red")
ax.findobj(matplotlib.patches.Patch)[1].set_facecolor("blue")
ax.findobj(matplotlib.patches.Patch)[2].set_facecolor("green")

##plt.title('Perimeter (pixels)',fontsize=12)
plt.show()

# calculate p-value ###
Cl=Cl.tolist()

Con=[]
for x in Cl:
    if math.isnan(x)==False:
        Con.append(x)
        
Pl=Pl.tolist()

Ps=[]
for x in Pl:
    if math.isnan(x)==False:
        Ps.append(x)
        
Nl=Nl.tolist()

Ns=[]
for x in Nl: 
    if math.isnan(x)==False:
        Ns.append(x)

# # # #plt.hist(D, normed=False, alpha=0.5,bins=15,color='green',cumulative=False)
# # #print(p)

PC=ttest_ind(a=np.array(Ps),b=np.array(Con),equal_var=True)
print(PC)

NC=ttest_ind(a=np.array(Ns),b=np.array(Con),equal_var=True)
print(NC)

NP=ttest_ind(a=np.array(Ns),b=np.array(Ps),equal_var=True)
print(NP)

