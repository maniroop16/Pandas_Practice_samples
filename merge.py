import pandas as pd
import numpy as np

cars1 = pd.read_csv(r"C:\WebDev\Python_Practice\pandas\Pandas_Latest\datasets\merge\merged1.csv")
cars2 = pd.read_csv(r"C:\WebDev\Python_Practice\pandas\Pandas_Latest\datasets\merge\merged2.csv")
cars1_new = cars1.loc[:, "mpg":"car"]
#cars1_new.size() This size function works only in case of using groupby else we have to use shape
#cars = cars1_new.merge(cars2, how="outer")
cars = cars1_new._append(cars2)

numpy_arr = np.random.randint(15000, 75000,size=398, dtype="L")
cars["owners"] = numpy_arr

print(cars)