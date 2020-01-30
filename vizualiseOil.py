import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


url ="C:/Users/Βασίλης/IdeaProjects/thesis_python_scripts/Data sets/Crude_Oil_Prices_Brent.csv"
print(url)

df = pd.read_csv(url)
series = np.array(df.Value)

plt.plot(series)
plt.show()