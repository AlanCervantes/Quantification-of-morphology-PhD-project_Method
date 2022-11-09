#libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


xl = pd.ExcelFile(r"/Users/ankita/Desktop/DataAnalysis/RGB/Procrustes/Re-analysis/Peter_Reanalysis/Data_Compile_AP_final_1.xlsx")
df = xl.parse('Nstress_violinplot')


ax=sns.violinplot(x='Root growth', y='PD_n', data=df)
ax.set(xlabel=None)
ax.set(ylabel=None)
plt.show()

