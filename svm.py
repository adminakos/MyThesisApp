from sklearn.svm import SVC
from matplotlib import pyplot as plt
import pandas as pd
from sklearn.svm import OneClassSVM

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
df = pd.read_csv('C:/Users/petro/Desktop/Timeseries.csv')
def clean(x):
    x = x.replace("/", "")
    return float(x)


df.Date = df.Date.apply(clean)
print(df.Date)
X = df.drop(['Value'], axis='columns')
y=df.Value

print(X)
print(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
print(len(X_train))
print(len(X_test))
model = SVC(gamma='auto')
print(len(y_train))
print(len(y_test))
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
y_pred = model.predict(X_test)
print(y_pred)


print(classification_report(y_test, y_pred))