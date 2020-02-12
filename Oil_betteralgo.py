import pandas as pd
from sklearn.metrics import mean_squared_log_error


expected = pd.read_csv("C:/Users/Βασίλης/IdeaProjects/MyThesisApp/JavaOut.csv")
x= len(expected)
# print(x)

# print(expected)
predictedsvm = pd.read_csv("C:/Users/Βασίλης/IdeaProjects/thesis_python_scripts/svmanomaliesoil.csv")
# print(predictedsvm['Value'])
y= len(predictedsvm['Value'])
# print(y)
z= abs(y-x)
# print(z)
for i in range(z):
    expected = expected.append(pd.Series([0], index=expected.columns ), ignore_index=True)

msleSVM = mean_squared_log_error(expected, predictedsvm['Value'])
print("SVM msle: %f " %msleSVM)
# ----------------------------------------------------------------------------------------------------------
expectedisol = pd.read_csv("C:/Users/Βασίλης/IdeaProjects/MyThesisApp/JavaOut.csv")
x1= len(expectedisol)
predictedisol = pd.read_csv("C:/Users/Βασίλης/IdeaProjects/thesis_python_scripts/isolationanomaliesoil.csv")
# print(predictedisol['Value'])
y1= len(predictedisol['Value'])

z1= abs(y1-x1)

for i in range(z1):
    expectedisol = expectedisol.append(pd.Series([0], index=expectedisol.columns ), ignore_index=True)

msleISOL = mean_squared_log_error(expectedisol, predictedisol['Value'])
print("Isolation Forest msle: %f " %msleISOL)
# ----------------------------------------------------------------------------------------------------------
expectedkmeans = pd.read_csv("C:/Users/Βασίλης/IdeaProjects/MyThesisApp/JavaOut.csv")

x2= len(expectedkmeans)
predictedkmeans = pd.read_csv("C:/Users/Βασίλης/IdeaProjects/thesis_python_scripts/kmeansOil.csv")
# print(predictedkmeans['Value'])
y2= len(predictedkmeans['Value'])

z2= abs(y2-x2)

for i in range(z2):
    predictedkmeans = predictedkmeans.append(pd.Series([0,'',0], index=predictedkmeans.columns ), ignore_index=True)

msleKMEANS = mean_squared_log_error(expectedkmeans, predictedkmeans['Value'])
print("K-Means msle: %f " %msleKMEANS)

if msleSVM < msleISOL and msleSVM < msleKMEANS:
    print("One Class SVM is working better based on mean squared logarithmic error!")
elif msleISOL < msleSVM and msleISOL < msleKMEANS:
    print("Isolation Forest is working better based on mean squared logarithmic error!")
elif msleKMEANS < msleSVM and msleKMEANS < msleISOL:
    print("K-Means is working better based on mean squared logarithmic error!")
