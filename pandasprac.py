import pandas as pd
pd.set_option("display.max_rows", 20)

chipo = pd.read_csv(r"C:\Users\10687590\OneDrive - LTIMindtree\Desktop\pandas\datasets\filter_sort.csv", sep = '\t')

#print(users.occupation.value_counts().head(5).index[3])
#print(round(users.age.mean()))
prices = [float(value[1 : ]) for value in chipo.item_price]
chipo.item_price = prices
#chipo.price_per_item = chipo.item_price/chipo.quantity

#print(chipo[chipo.price_per_item > 10])
#print(chipo[(chipo['item_name'] == 'Chicken Bowl') & (chipo['quantity'] == 1)])

"""new_df = chipo[['item_name','item_price']]
print(new_df)"""

#print(chipo.sort_values(by = "item_price",ascending = False).head(1))
cannon_soda = chipo[(chipo.item_name == "Canned Soda") &(chipo.quantity >1)].shape[0]
print(cannon_soda)
remove_duplicates = chipo.drop_duplicates(['item_name','quantity','choice_description'])
one_quntity = remove_duplicates[remove_duplicates.quantity == 1]
#print(one_quntity[one_quntity.item_price > 10])