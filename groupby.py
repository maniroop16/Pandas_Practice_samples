import pandas as pd

drinks = pd.read_csv(r"C:\Users\10687590\OneDrive - LTIMindtree\Desktop\pandas\datasets\groupby.csv")
#round(drinks.groupby('continent').beer_servings.mean(),2)
#drinks.groupby("continent").wine_servings.describe()

#drinks.groupby('continent').spirit_servings.agg(["min","max"])
#or
#drinks.groupby('continent').agg({"spirit_servings":["min","max"]})
print()