import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import warnings

warnings.filterwarnings("ignore")

df = pd.read_csv("Online_Retail.csv")
df = df[df['Quantity']>0]

df = df.dropna(axis=0, subset=['InvoiceNo'])
df = df[~df['InvoiceNo'].str.contains('C')]

data = df[df["Country"] == "United Kingdom"]
temp1 = data.groupby(by=["InvoiceNo", "Description"])["Quantity"].sum()
# temp1
data = temp1.unstack().fillna(0)
data.columns.name = None
# data

data = data.map(lambda x : 0 if x<= 0 else 1)
data = data[data.sum(axis=1) >= 2]

from mlxtend.frequent_patterns import apriori

frequent_itemsets = apriori(data, min_support=0.03, use_colnames=True).sort_values(by="support", ascending=False).reset_index(drop=True)
frequent_itemsets["length"] = frequent_itemsets["itemsets"].apply(lambda x : len(x))

print(frequent_itemsets)


from mlxtend.frequent_patterns import association_rules

association_rule_matrix = association_rules(frequent_itemsets, metric="lift", min_threshold=1).sort_values(by="lift", ascending=False).reset_index(drop=True)
print(association_rule_matrix)