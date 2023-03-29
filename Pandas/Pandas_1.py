# First Pandas course file
import pandas as pd
import numpy as np
# With below line you can see pandas version
version = (pd.__version__)
my_data = [10, 20, 30]
my_index = [1, 2, 3]

my_serie = pd.Series(data=my_data, index=my_index)
print(my_serie)
