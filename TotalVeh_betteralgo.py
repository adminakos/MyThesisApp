from sklearn.svm import OneClassSVM
from sklearn.metrics import mean_squared_log_error
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
from saxpy.visit_registry import VisitRegistry
from saxpy.distance import early_abandoned_dist
from saxpy.znorm import znorm


expected = pd.read_csv("C:/Users/Βασίλης/IdeaProjects/MyThesisApp/JavaOut.csv")
x= len(expected)

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
print("SVM msle: %f"%msleSVM)
# ----------------------------------------------------------------------------------------------------------
expectedisol = pd.read_csv("C:/Users/Βασίλης/IdeaProjects/MyThesisApp/JavaOut.csv")
x1= len(expectedisol)


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
predictedisol = a

y1= len(predictedisol['Value'])

z1= abs(y1-x1)

for i in range(z1):
    if x1 < y1:
        expectedisol = expectedisol.append(pd.Series([0], index=expectedisol.columns ), ignore_index=True)
    elif y1 < x1:
        predictedisol = predictedisol.append(pd.Series([0,'',0], index=predictedisol.columns ), ignore_index=True)
msleISOL = mean_squared_log_error(expectedisol, predictedisol['Value'])
print("Isolation Forest msle: %f"%msleISOL)
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
print("KMeans msle: %f"%msleKMEANS)
# ----------------------------------------------------------------------------------------------------------
expectedZscore = pd.read_csv("C:/Users/Βασίλης/IdeaProjects/MyThesisApp/JavaOut.csv")

x5= len(expectedZscore)



url = "C:/Users/Βασίλης/IdeaProjects/MyThesisApp/Data sets/Total_Vehicle_Sales.csv"
df = pd.read_csv(url)

def clean(x):
    x = x.replace("/", "").replace("-", "")
    return float(x)


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

    return outliers

outlier_datapoints = detect_outlier(series)


y=len(df['Value'])
df2  =pd.DataFrame(outlier_datapoints, columns= ['Value'])

x=len(outlier_datapoints)
z=abs(y-x)
for i in range(z):
    df2 = df2.append(pd.Series([0], index=df2.columns ), ignore_index=True)

df = df.assign(anomaly=df['Value'].isin(df2['Value']).astype(int))


a=df.loc[df['anomaly'] == 1 , ['Date', 'Value']]
predictedZscore = a

y5= len(predictedZscore['Value'])

z5= abs(y5-x5)

for i in range(z5):
    if x5 < y5:
        expectedZscore = expectedZscore.append(pd.Series([0], index=expectedZscore.columns ), ignore_index=True)
    elif y5 < x5:
        predictedZscore = predictedZscore.append(pd.Series([0,0], index=predictedZscore.columns ), ignore_index=True)

msleZscore = mean_squared_log_error(expectedZscore, predictedZscore['Value'])
print("Zscore msle: %f"%msleZscore)
#-----------------------------------------------------------------------------------------------------------
expectedSAX = pd.read_csv("C:/Users/Βασίλης/IdeaProjects/MyThesisApp/JavaOut.csv")

xs= len(expectedSAX)
url = "C:/Users/Βασίλης/IdeaProjects/MyThesisApp/Data sets/Total_Vehicle_Sales.csv" #dialog box and return the path to the selected file

df = pd.read_csv(url)

series = np.array(df.Value)

def find_best_discord_brute_force(series, win_size , global_registry,
                                  z_threshold=0.01):
    """Early-abandoned distance-based discord discovery."""
    best_so_far_distance = -1.0
    best_so_far_index = -1

    outerRegistry = global_registry.clone()

    outer_idx = outerRegistry.get_next_unvisited()

    while ~np.isnan(outer_idx):

        outerRegistry.mark_visited(outer_idx)

        candidate_seq = znorm(series[outer_idx:(outer_idx+win_size)],
                              z_threshold)

        nnDistance = np.inf
        innerRegistry = VisitRegistry(len(series) - win_size)

        inner_idx = innerRegistry.get_next_unvisited()

        while ~np.isnan(inner_idx):
            innerRegistry.mark_visited(inner_idx)

            if abs(inner_idx - outer_idx) > win_size:

                curr_seq = znorm(series[inner_idx:(inner_idx+win_size)],
                                 z_threshold)
                dist = early_abandoned_dist(candidate_seq,
                                            curr_seq, nnDistance)

                if (~np.isnan(dist)) and (dist < nnDistance):
                    nnDistance = dist

            inner_idx = innerRegistry.get_next_unvisited()

        if ~(np.inf == nnDistance) and (nnDistance > best_so_far_distance):
            best_so_far_distance = nnDistance
            best_so_far_index = outer_idx

        outer_idx = outerRegistry.get_next_unvisited()

    return best_so_far_index
# print(len(series))

def find_discords_brute_force(series, win_size = 1, num_discords=12,
                              z_threshold=0.01):
    """Early-abandoned distance-based discord discovery."""
    discords = list()

    globalRegistry = VisitRegistry(len(series))
    globalRegistry.mark_visited_range(len(series) - win_size, len(series))

    while (len(discords) < num_discords):

        bestDiscord = find_best_discord_brute_force(series, win_size,
                                                    globalRegistry,
                                                    z_threshold)

        if -1 == bestDiscord:
            break

        discords.append(bestDiscord)

        mark_start = bestDiscord - win_size
        if 0 > mark_start:
            mark_start = 0

        mark_end = bestDiscord + win_size
        '''if len(series) < mark_end:
            mark_end = len(series)'''

        globalRegistry.mark_visited_range(mark_start, mark_end)

    return discords

p = df.index.values
df.insert( 0, column="new",value = p)
ys1=len(df['Value'])
xaa=find_discords_brute_force(series)

df2  =pd.DataFrame(xaa, columns= ['Value'])

xs1=len(find_discords_brute_force(series))
zs1=abs(ys1-xs1)
for i in range(zs1):
    df2 = df2.append(pd.Series([0], index=df2.columns ), ignore_index=True)

df = df.assign(anomaly=df['new'].isin(df2['Value']).astype(int))

a=df.loc[df['anomaly'] == 1 , ['Date', 'Value']]
predictedSAX = a

ys= len(predictedSAX['Value'])

zs= abs(ys-xs)

for i in range(zs):
    if xs < ys:
        expectedSAX = expectedSAX.append(pd.Series([0], index=expectedSAX.columns ), ignore_index=True)
    elif ys < xs:
        predictedSAX = predictedSAX.append(pd.Series([0,0], index=predictedSAX.columns ), ignore_index=True)

msleSAX = mean_squared_log_error(expectedSAX, predictedSAX['Value'])
print("S.A.X. msle: %f"%msleSAX)


if msleSVM < msleISOL and msleSVM < msleKMEANS and msleSVM < msleZscore and msleSVM < msleSAX:
    print("One Class SVM is working better based on mean squared logarithmic error!")
elif msleISOL < msleSVM and msleISOL < msleKMEANS and msleISOL < msleZscore and msleISOL < msleSAX:
    print("Isolation Forest is working better based on mean squared logarithmic error!")
elif msleKMEANS < msleSVM and msleKMEANS < msleISOL and msleKMEANS < msleZscore and msleKMEANS < msleSAX:
    print("K-Means is working better based on mean squared logarithmic error!")
elif msleZscore < msleSVM and msleZscore < msleISOL and msleZscore < msleKMEANS and msleZscore < msleSAX:
    print("Z-score is working better based on mean squared logarithmic error!")
elif msleSAX < msleZscore and msleSAX < msleSVM and msleSAX < msleISOL and msleSAX < msleKMEANS:
    print("S.A.X. is working better based on mean squared logarithmic error!")

