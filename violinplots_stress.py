#libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


xl = pd.ExcelFile(r"Data_Files_Morphology/Data_Compile_AP_final_1.xlsx")
df = xl.parse('Nstress_violinplot')


ax=sns.violinplot(x='Root growth', y='PD_n', data=df)
ax.set(xlabel=None)
ax.set(ylabel=None)
plt.show()

