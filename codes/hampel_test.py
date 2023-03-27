import matplotlib.pyplot as plt
import pandas as pd
from hampel import hampel

ts = pd.Series([1, 2, 1 , 1 , 1, 2, 13, 2, 1, 2, 15, 1, 2])

# Just outlier detection
outlier_indices = hampel(ts, window_size=9, n=3)
print("Outlier Indices: ", outlier_indices)

# Outlier Imputation with rolling median
ts_imputation = hampel(ts, window_size=5, n=3, imputation=True)

ts.plot(style="k-")
ts_imputation.plot(style="g-")
plt.show()