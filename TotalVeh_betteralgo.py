from sklearn.svm import OneClassSVM
from sklearn.metrics import mean_squared_log_error
from sklearn.ensemble import IsolationForest
import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.cluster import KMeans

expected = pd.read_csv("C:/Users/Βασίλης/IdeaProjects/MyThesisApp/JavaOut.csv")
x= len(expected)

url ="C:/Users/Βασίλης/IdeaProjects/MyThesisApp/Data sets/Total_Vehicle_Sales.csv"
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


a = dataset.loc[dataset['anomaly'] == -1, ['Date', 'Value']] #anomaly


predictedsvm = a

y= len(predictedsvm['Value'])

z= abs(y-x)

for i in range(z):
    if x < y:
        expected = expected.append(pd.Series([0], index=expected.columns ), ignore_index=True)
    elif y < x:
        predictedsvm = predictedsvm.append(pd.Series([0,'',0], index=predictedsvm.columns ), ignore_index=True)
msleSVM = mean_squared_log_error(expected, predictedsvm['Value'])
print(msleSVM)
# ----------------------------------------------------------------------------------------------------------
expectedisol = pd.read_csv("C:/Users/Βασίλης/IdeaProjects/MyThesisApp/JavaOut.csv")
x1= len(expectedisol)


url ="C:/Users/Βασίλης/IdeaProjects/MyThesisApp/Data sets/Total_Vehicle_Sales.csv"
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


a = dataset.loc[dataset['anomaly2'] == -1, ['Date', 'Value']] #anomaly
predictedisol = a

y1= len(predictedisol['Value'])

z1= abs(y1-x1)

for i in range(z1):
    if x1 < y1:
        expectedisol = expectedisol.append(pd.Series([0], index=expectedisol.columns ), ignore_index=True)
    elif y1 < x1:
        predictedisol = predictedisol.append(pd.Series([0,'',0], index=predictedisol.columns ), ignore_index=True)
msleISOL = mean_squared_log_error(expectedisol, predictedisol['Value'])
print(msleISOL)
# ----------------------------------------------------------------------------------------------------------
expectedkmeans = pd.read_csv("C:/Users/Βασίλης/IdeaProjects/MyThesisApp/JavaOut.csv")

x2= len(expectedkmeans)



url = "C:/Users/Βασίλης/IdeaProjects/MyThesisApp/Data sets/Total_Vehicle_Sales.csv"
df = pd.read_csv(url)


data = df[['Value']]
n_cluster = range(1, 20)
kmeans = [KMeans(n_clusters=i).fit(data) for i in n_cluster]
scores = [kmeans[i].score(data) for i in range(len(kmeans))]
X = df[['Value']]
X = X.reset_index(drop=True)
km = KMeans(n_clusters=10)
km.fit(X)
km.predict(X)
labels = km.labels_

def getDistanceByPoint(data, model):
    distance = pd.Series()
    for i in range(0,len(data)):
        Xa = np.array(data.loc[i])
        Xb = model.cluster_centers_[model.labels_[i]-1]
        distance.set_value(i, np.linalg.norm(Xa-Xb))
    return distance

outliers_fraction = 0.055
# get the distance between each point and its nearest centroid. The biggest distances are considered as anomaly
distance = getDistanceByPoint(data, kmeans[1])
number_of_outliers = int(outliers_fraction*len(distance))
threshold = distance.nlargest(number_of_outliers).min()
# anomaly1 contain the anomaly result of the above method Cluster (0:normal, 1:anomaly)
df['anomaly1'] = (distance >= threshold).astype(int)

a=df.loc[df['anomaly1'] == 1 , ['Date', 'Value']]
predictedkmeans = a

y2= len(predictedkmeans['Value'])

z2= abs(y2-x2)

for i in range(z2):
    if x2 < y2:
        expectedkmeans = expectedkmeans.append(pd.Series([0], index=expectedkmeans.columns ), ignore_index=True)
    elif y2 < x2:
        predictedkmeans = predictedkmeans.append(pd.Series([0,0], index=predictedkmeans.columns ), ignore_index=True)

msleKMEANS = mean_squared_log_error(expectedkmeans, predictedkmeans['Value'])
print(msleKMEANS)

if msleSVM < msleISOL and msleSVM < msleKMEANS:
    print("One Class SVM is working better based on mean squared logarithmic error!")
elif msleISOL < msleSVM and msleISOL < msleKMEANS:
    print("Isolation Forest is working better based on mean squared logarithmic error!")
elif msleKMEANS < msleSVM and msleKMEANS < msleISOL:
    print("K-Means is working better based on mean squared logarithmic error!")
