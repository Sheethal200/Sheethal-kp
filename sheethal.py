import pandas as pd
from matplotlib import pyplot as plt
data=pd.read_csv("aircrashesFullData.csv")
dataframe=pd.DataFrame(data)
dfh=dataframe.head(20)
dfh.plot(x="Country/Region",y="Year",title="Air Crashes Data")
plt.show()