
## Analyze the development of the morphology of a 'hooked' hair in N-stress, Control & P-stress ##


#libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#libraries

xl = pd.ExcelFile(r"Data_Files_Morphology/Data_Compile_AP_final_1.xlsx")

def violinplot(xl,stress):
  xl = pd.ExcelFile(r"Data_Files_Morphology/Data_Compile_AP_final_1.xlsx")
  df = xl.parse(stress)
  ax=sns.violinplot(x='Root growth', y='PD_n', data=df)
  ax.set(xlabel=None)
  ax.set(ylabel=None)
  plt.show()
  return()


violinplot(xl,'Nstress_violinplot')
violinplot(xl,'Pstress_violinplot')
violinplot(xl,'Control_violinplot')
