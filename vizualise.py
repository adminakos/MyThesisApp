import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


url ="C:/Users/Βασίλης/IdeaProjects/MyThesisApp/Data sets/Total_Vehicle_Sales.csv"
print(url)

df = pd.read_csv(url)
series = np.array(df.Value)

plt.plot(series)
plt.show()