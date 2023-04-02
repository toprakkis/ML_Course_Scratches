# First Pandas course file
import pandas as pd
import numpy as np

# Just to get same random values
np.random.seed(42)


# With below line you can see pandas version
version = (pd.__version__)
my_data = [10, 20, 30]
my_index = [1, 2, 3]

# Supplying data and index to Pandas Series
my_serie = pd.Series(data=my_data, index=my_index)

sample_dict = {"a": 10, "b": 20}

# Pandas Series takes keys as index and values as data automatically

my_serie = pd.Series(data=sample_dict)
print(my_serie)

# .keys() gives indexes of the Pandas Serie
print(my_serie.keys())

df = pd.read_csv(r"Pandas\tips.csv")

df = pd.DataFrame(df)
# df.columns and df.index for column and index
# df.info() gives necessary info on dataframe
print(df.info())
# df.describe() gives statistical info
print(df.describe())
