
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.svm import OneClassSVM


url ="C:/Users/Βασίλης/IdeaProjects/MyThesisApp/Data sets/Total_Vehicle_Sales.csv"
dataset = pd.read_csv(url)

outliers_fraction = 0.05

data = dataset[['Value']]
scaler = StandardScaler()
np_scaled = scaler.fit_transform(data)
data = pd.DataFrame(np_scaled)
# train oneclassSVM
model = OneClassSVM(nu=outliers_fraction, kernel='rbf', gamma=0.01)

model.fit(data)

dataset['anomaly'] = pd.Series(model.predict(data))

print(dataset)

a = dataset.loc[dataset['anomaly'] == -1, ['Date', 'Value']] #anomaly


fig, ax = plt.subplots(figsize=(15,10))
ax.plot(dataset['Date'], dataset['Value'], color='blue')
ax.scatter(a['Date'],a['Value'], color='red', label = 'Anomaly Detection OneClassSVM')
plt.show()

# original = []
# anomalies = []
# for count in a:
#
#     if(dataset['anomaly'].any == -1):
#         print("anomaly")
#         original.append(dataset['Value'])
#         anomalies.append("anomaly")
#
#
# print(original)
# print(anomalies)
# anomalieslist = pd.DataFrame(
#     {'Value': original,
#      'anomaly': anomalies,
#      })

