import pandas as pd
import numpy as np

a = np.random.randint(1,4,size=100)
b = np.random.randint(1,3,size=100)
c = np.random.randint(10000,30000,size=100)

s1 = pd.Series(a)
s2 = pd.Series(b)
s3 = pd.Series(c)

df = pd.concat([s1,s2,s3], axis= 1)
df.columns = ["bedrs","bathrs","price_sqr_meter"]
big_column = pd.concat([s1,s2,s3], axis=0)
big_column = big_column.to_frame()

big_column.reset_index(inplace=True,drop=True) # This will reset the index and assign from 0 
print(big_column)