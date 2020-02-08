import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from tslearn.piecewise import PiecewiseAggregateApproximation
from tslearn.piecewise import SymbolicAggregateApproximation


url ="C:/Users/Βασίλης/IdeaProjects/MyThesisApp/Data sets/Total_Vehicle_Sales.csv"

df = pd.read_csv(url)
series = np.array(df.Value)
print(series)

n_paa_segments = 4
paa = PiecewiseAggregateApproximation(n_segments=n_paa_segments)
paa_dataset_inv = paa.inverse_transform(paa.fit_transform(series))
plt.plot(series.ravel(), "b-", alpha=0.4)
plt.plot(paa_dataset_inv.ravel(), "r-")



n_sax_symbols = 4
sax = SymbolicAggregateApproximation(n_segments=n_paa_segments, alphabet_size_avg=n_sax_symbols)
print(sax)
sax_dataset_inv = sax.inverse_transform(sax.fit_transform(series))
print(sax_dataset_inv.ravel())

plt.plot(sax_dataset_inv.ravel(), "y-")
plt.title("SAX, %d symbols" % n_sax_symbols)
plt.show()