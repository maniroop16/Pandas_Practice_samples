import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

titanic = pd.read_csv(r"C:\Users\10687590\OneDrive - LTIMindtree\Desktop\pandas\datasets\visualization.csv", index_col="PassengerId")

print(titanic[0])

'''titanic.plot.pie()
plt.show()'''