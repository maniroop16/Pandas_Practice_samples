import pandas as pd

euro12 = pd.read_csv(r"C:\Users\10687590\OneDrive - LTIMindtree\Desktop\pandas\datasets\filterandsort2.csv")
#print(euro12.columns)

#discipline = euro12[["Team","Yellow Cards","Red Cards"]]

#discipline.sort_values(by = ["Red Cards","Yellow Cards"])
#round(discipline["Yellow Cards"].mean())
#euro12[euro12.Team.str.endswith('e')]
#euro12.iloc[:,0:7] gives all the rows with forst 7 columns
#euro12.iloc[:,0:-3] selecting all the rows and columns except last 3

#print(euro12.loc[["England","Italy","Russia"],"Shooting Accuracy"])
# euro12.loc[euro12.Team.isin(['England', 'Italy', 'Russia']),["Team","Shooting Accuracy"]] this will 
# give shooting accuracy of 3 teams
print(euro12.loc[euro12.Team.isin(['England', 'Italy', 'Russia']),["Team","Shooting Accuracy"]])