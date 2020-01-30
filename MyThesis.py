import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from tkinter.filedialog import askopenfilename
from sklearn.preprocessing import StandardScaler
from sklearn.externals import joblib
from sklearn.svm import OneClassSVM
from sklearn.ensemble import IsolationForest
from tslearn.piecewise import PiecewiseAggregateApproximation
from tslearn.piecewise import SymbolicAggregateApproximation


url = askopenfilename() #dialog box and return the path to the selected file
print(url)

# df = pd.read_csv(url)
# series = np.array(df.Value)
# print(series)
#
# n_paa_segments = 4
# paa = PiecewiseAggregateApproximation(n_segments=n_paa_segments)
# paa_dataset_inv = paa.inverse_transform(paa.fit_transform(series))
# plt.plot(series.ravel(), "b-", alpha=0.4)
# plt.plot(paa_dataset_inv.ravel(), "r-")
#
#
#
# n_sax_symbols = 4
# sax = SymbolicAggregateApproximation(n_segments=n_paa_segments, alphabet_size_avg=n_sax_symbols)
# print(sax)
# sax_dataset_inv = sax.inverse_transform(sax.fit_transform(series))
# print(sax_dataset_inv.ravel())
#
# plt.plot(sax_dataset_inv.ravel(), "y-")
# plt.title("SAX, %d symbols" % n_sax_symbols)
# plt.show()
#


dataset = pd.read_csv(url)

outliers_fraction = 0.30

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

ax2.plot(dataset['Date'], dataset['Value'], color='blue', label = 'Normal')
ax2.scatter(a['Date'],a['Value'], color='red', label = 'Anomaly Detection IsolationForest')
plt.legend()

plt.show()

