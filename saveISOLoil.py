from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler

url ="C:/Users/Βασίλης/IdeaProjects/thesis_python_scripts/Data sets/Crude_Oil_Prices_Brent.csv"
dataset = pd.read_csv(url)
data = dataset[['Value']]
outliers_fraction = 0.25
scaler = StandardScaler()
np_scaled = scaler.fit_transform(data)
data = pd.DataFrame(np_scaled)
# train isolation forest
model =  IsolationForest(behaviour = 'new', max_samples=100, random_state=1, contamination= outliers_fraction)
model.fit(data)
dataset['anomaly2'] = pd.Series(model.predict(data))
# visualization
fig2, ax2 = plt.subplots(figsize=(10,6))

a = dataset.loc[dataset['anomaly2'] == -1, ['Date', 'Value']] #anomaly
a.to_csv('isolationanomaliesoil.csv')
