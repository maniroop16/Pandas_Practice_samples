import pandas as pd

df = pd.read_csv(r"C:\Users\10687590\OneDrive - LTIMindtree\Desktop\pandas\datasets\apply.csv")
refined_df = df.loc[:,"school":"guardian"]

#refined_df.apply(lambda x: str(x).capitalize())

capitalizer = lambda x: x.capitalize()
refined_df["Mjob"] = refined_df["Mjob"].apply(capitalizer)

def cal_age(x):
    if x>17:
        return True
    else:
        return False

refined_df["legal_drinker"] = refined_df["age"].apply(cal_age)

def mul_ten(x):
    if type(x) is int:
        return x*10
    return x

refined_df.applymap(mul_ten).head() # this will check the integer values in the dataset and multply by 10
print()