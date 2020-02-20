import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from tkinter.filedialog import askopenfilename

def clean(x):
    x = x.replace("/", "").replace("-", "")
    return float(x)

url = "C:/Users/Βασίλης/IdeaProjects/MyThesisApp/Data sets/Total_Vehicle_Sales.csv"
print(url)
df = pd.read_csv(url)
series = np.array(df.Value)
outliers=[]
df.Date = df.Date.apply(clean)
def detect_outlier(data_1):

    threshold=2
    mean_1 = np.mean(data_1)
    std_1 =np.std(data_1)


    for y in data_1:
        z_score= (y - mean_1)/std_1
        if np.abs(z_score) > threshold:
            outliers.append(y)

    return outliers
# print(series)
outlier_datapoints = detect_outlier(series)
print(outlier_datapoints)

y=len(df['Value'])
df2  =pd.DataFrame(outlier_datapoints, columns= ['Value'])
print(outlier_datapoints)
x=len(outlier_datapoints)
z=abs(y-x)
for i in range(z):
    df2 = df2.append(pd.Series([0], index=df2.columns ), ignore_index=True)

df = df.assign(anomaly=df['Value'].isin(df2['Value']).astype(int))

colors = ['r' if anomaly==1 else 'b' for anomaly in df.anomaly]

plt.plot(df['Date'], df['Value'], color='blue', linewidth=1)

plt.scatter(df['Date'], df['Value'], color=colors, linewidths=0)
plt.show()
