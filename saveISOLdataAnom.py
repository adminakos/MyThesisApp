from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler

url ="C:/Users/Βασίλης/IdeaProjects/MyThesisApp/Data sets/Total_Vehicle_Sales.csv"
dataset = pd.read_csv(url)
data = dataset[['Value']]
outliers_fraction = 0.06
scaler = StandardScaler()
np_scaled = scaler.fit_transform(data)
data = pd.DataFrame(np_scaled)
# train isolation forest
model =  IsolationForest(behaviour = 'new', max_samples=100, random_state=1, contamination= outliers_fraction)
model.fit(data)
dataset['anomaly2'] = pd.Series(model.predict(data))


a = dataset.loc[dataset['anomaly2'] == -1, ['Date', 'Value']] #anomaly
a.to_csv('isolationanomaliessales.csv')
