import numpy as np
import pandas as pd

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

    threshold=1.7
    mean_1 = np.mean(data_1)
    std_1 =np.std(data_1)
    count=0

    for y in data_1:
        z_score= (y - mean_1)/std_1
        if np.abs(z_score) > threshold:
            outliers.append(y)
            count+=1
        print(z_score)

        print(count)
    return outliers
print(series)
outlier_datapoints = detect_outlier(series)
print(outlier_datapoints)

y=len(df['Value'])
df2  =pd.DataFrame(outlier_datapoints, columns= ['Value'])
print(df2)

df = df.assign(anomaly=df['Value'].isin(df2['Value']).astype(int))

a=df.loc[df['anomaly'] == 1 , ['Date', 'Value']]
a.to_csv("TotalVZscoreAnom.csv")

