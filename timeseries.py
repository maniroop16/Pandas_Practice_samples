import pandas as pd

apple = pd.read_csv(r'C:\Users\10687590\OneDrive - LTIMindtree\Desktop\pandas\datasets\timeseries.csv')
apple.Date = pd.to_datetime(apple["Date"])
apple.set_index("Date", inplace=True)
#apple.duplicated() This will give duplicated rows
#apple.columnname.is_unique()  This is to check specific columns duplicated or unique

#apple_month = apple.resample('BME').mean()
# (apple.index.max() - apple.index.min()).days  #No of days from first to last
print()