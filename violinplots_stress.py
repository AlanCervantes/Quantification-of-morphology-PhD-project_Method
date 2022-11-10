
## Analyze the area, perimeter, length and shape of the 'hooked' hairs in early development according to age and root growth for each treatment ##

#libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


xl = pd.ExcelFile(r"Data_Compile_AP_final_1.xlsx")
df = xl.parse('Nstress_violinplot')


ax=sns.violinplot(x='Root growth', y='PD_n', data=df)
ax.set(xlabel=None)
ax.set(ylabel=None)
plt.show()

