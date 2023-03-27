import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

csv = 'Report_25112022145648_Dominant_Pollutant.csv'


cmap, norm = mcolors.from_levels_and_colors([0, 50, 100, 200, 250], ['green', 'yellow', 'red','purple'])
df = pd.read_csv(csv)
print(df)

col = []
for val in df['Data']:
    if val < 50:
        col.append('green')
    elif val >=50 and val < 100:
        col.append('yellow')
    elif val >= 100 and val < 200:
        col.append('red')
    elif val >= 200:
        col.append('purple')
    else:
        col.append('white')
#plt.figure(figsize=(16,9))
df.plot(x='Time', y='Data', figsize=(16,9),xlabel='Time',ylabel='AQI', kind='bar', color=col)
plt.autoscale()
plt.xticks(rotation=90)
plt.xlim(30,90)
plt.title("AQI Noviembre 2022", fontsize=20)
#plt.grid()
plt.legend()
plt.savefig('aqi_nov.png', bbox_inches="tight", dpi=300, transparent=True)
#plt.savefig('aqi_nov.png')
plt.show()