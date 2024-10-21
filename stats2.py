import pandas as pd
import datetime

df = pd.read_csv(r"C:\Users\10687590\OneDrive - LTIMindtree\Desktop\pandas\datasets\stats2.csv", sep="\s+", parse_dates = [[0,1,2]])

def fix_century(x):
    year = x.year
    if year > 1989:
        year = x.year - 100 
    return datetime.date(year, x.month, x.day)

df["Yr_Mo_Dy"] = df["Yr_Mo_Dy"].apply(fix_century)   
df["Yr_Mo_Dy"] = pd.to_datetime(df["Yr_Mo_Dy"])


df = df.set_index("Yr_Mo_Dy")
#df.isnull().sum()
#df.notnull().sum()
print()
#df.sum().sum() - df.notnull().sum().sum()

#df.agg(["min","max","mean","std"],axis=1) # column wise (Min of all the column in the row)

#df.agg(["min","max","mean","std"]) # row wise(Min of all the rows in the column)
#df.loc[df.index.month == 1].mean()
#df.groupby(df.index.to_period('A')).mean() This is to downsample the record by year 
#df.groupby(df.index.to_period('M')).mean() This is to downsample the record by Month 
#df.groupby(df.index.to_period('W')).mean() This is to downsample the record by Week 

# resample data to 'W' week and use the functions
weekly = df.resample('W').agg(['min','max','mean','std'])

# slice it for the first 52 weeks and locations
weekly.loc[weekly.index[1:53], "RPT":"MAL"] .head(10)

print()
