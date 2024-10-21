import pandas as pd

baby_names = pd.read_csv(r"C:\Users\10687590\OneDrive - LTIMindtree\Desktop\pandas\datasets\stats.csv")

del baby_names["Unnamed: 0"]
del baby_names["Id"]
del baby_names["Year"]
baby_names.groupby("Gender").count() # This gives all the colunms count by grouping Gender column

baby_names.Gender.value_counts() #Exact value count of Genders

names = baby_names.groupby("Name").sum()
names.sort_values("Count", ascending=False)
#print(len(names))

names[names.Count == names.Count.max()] # Most frequent occured name in dataset format
names.Count.idxmax() #  Most frequent occured name by direct value
names[names.Count == names.Count.min()] # min value occurance
names[names.Count == names.Count.median()] # Median value dataset
names.Count.std() # Starand deviation

print(names.describe())
