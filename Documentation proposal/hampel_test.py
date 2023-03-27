##
#@file: hampel.py
#@version: 1.1
#@brief: statistical technique used for outlier detection and robust data analysis
#@author: ----
#@documentation: Manuel Estrada & ---
#@date: --/--/----
#

#MODULES
import matplotlib.pyplot as plt
import pandas as pd
from hampel import hampel

#Create a labeled vector
ts = pd.Series([1, 2, 1 , 1 , 1, 2, 13, 2, 1, 2, 15, 1, 2])

# Just outlier detection
outlier_indices = hampel(ts, window_size=9, n=3)
print("Outlier Indices: ", outlier_indices)

# Outlier Imputation with rolling median
ts_imputation = hampel(ts, window_size=5, n=3, imputation=True)#Define window to hampel method result

#Plot hampel data
ts.plot(style="k-")
ts_imputation.plot(style="g-")
plt.show()
