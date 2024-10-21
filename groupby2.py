import pandas as pd
pd.set_option("display.max_column",30)

raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'], 
        'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'], 
        'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'], 
        'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}

regiment = pd.DataFrame(raw_data)
#regiment[regiment.regiment == "Nighthawks"].groupby("regiment").mean()
#regiment.groupby("company").describe()
#round(regiment.groupby("company").preTestScore.mean(),2)
#regiment.groupby(["regiment","company"]).preTestScore.mean()
#regiment.groupby(['regiment', 'company']).preTestScore.mean().unstack() #This gives without hyrarical indexing
#regiment.groupby(['regiment', 'company']).mean()
#regiment.groupby(['regiment', 'company']).count() Returns all the count
#regiment.groupby(['regiment', 'company']).size() returns no of observations
#print(regiment)

# regiment.groupby("regiment") This object contains unique names of that groupby column
#  and datasets of that names

'''for i,j in regiment.groupby("regiment"):
    print(j)'''


    
