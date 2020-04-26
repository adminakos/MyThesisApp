
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.svm import OneClassSVM
from sklearn.metrics import mean_squared_error, mean_squared_log_error



url ="C:/Users/Βασίλης/IdeaProjects/MyThesisApp/Data sets/Crude_Oil_Prices_Brent.csv"
dataset = pd.read_csv(url)

outliers_fraction = 0.055

data = dataset[['Value']]
scaler = StandardScaler()
np_scaled = scaler.fit_transform(data)
data = pd.DataFrame(np_scaled)
# train oneclassSVM
model = OneClassSVM(nu=outliers_fraction, kernel='rbf', gamma=0.01)

model.fit(data)
dataset['anomaly'] = pd.Series(model.predict(data))
print(dataset)
# print(model.score_samples(dataset['anomaly']))

a = dataset.loc[dataset['anomaly'] == -1, ['Date', 'Value']] #anomaly

a.to_csv('svmanomaliesoil.csv')

