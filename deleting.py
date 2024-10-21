import pandas as pd
import numpy as np

wine = pd.read_csv(r"C:\Users\10687590\OneDrive - LTIMindtree\Desktop\pandas\datasets\deleting.csv")
wine = wine.drop(wine.columns[[0,3,6,8,11,12,13]],axis=1)
#wine.dropna(subset=["alcohol"],inplace=True) Delete Null values in specific column
#wine.dropna(axis = 0, how = "any", inplace=True) Delete Null values in all the df
wine.columns = ["alcohol","malic_acid","alcalinity_of_ash","magnesium","flavanoids","proanthocyanins","hue"]

#wine.iloc[0:3,0] = np.nan #To show and replace the data use iloc fro mentioning integer values
'''wine.loc[0:2,"alcohol"] = np.nan # To show and reploce at specific places use loc for mentioning string
wine.loc[3:4,"magnesium"] = np.nan


wine.alcohol.fillna(10, inplace=True)
wine.magnesium.fillna(100, inplace=True)'''
#wine.isnull().sum()
'''random_nums = np.random.randint(10,size = 10)
wine.loc[random_nums,"alcohol"] = np.nan
wine.loc[11,"magnesium"] = np.nan
wine.drop(index=13,axis=0)'''
wine.loc[0:2,"alcohol"] = np.nan
allnullvalues = wine.alcohol.notnull()
wine.alcohol[allnullvalues]
wine = wine.reset_index(drop = True)
print(wine)