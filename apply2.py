import pandas as pd

crime = pd.read_csv(r"C:\Users\10687590\OneDrive - LTIMindtree\Desktop\pandas\datasets\apply2.csv")
#crime["Year"] = crime["Year"].astype("datetime64[ns]") This is used to convert from one dtype to another
crime.Year = pd.to_datetime(crime["Year"], format = "%Y") 
#This is for coverting a dtype to datetime type based on format mentioned
crime = crime.set_index("Year", drop=True)

crimes = crime.resample('10AS').sum()
max_population = crime["Population"].resample("10AS").max()

#*** resample function will change the length of the dataset to the 
# multiple valuse mentioned in the parameter 
# Note: This resample can be used only with dateandtime ***

crimes.Population = max_population

crime.idxmax(0) # if we want ro get max of all the columns in specific years
#Note: This idxmax can be used only with dateandtime
print(crime.idxmax(0))