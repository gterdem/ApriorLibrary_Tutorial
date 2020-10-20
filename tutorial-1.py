# products = ["Apple","Beer","Rice","Meat","Milk", "Pear"]

# t1 = (products[0], products[1], products[2], products[3] )
# t2 = (products[0], products[1], products[2] )
# t3 = (products[0], products[1] )
# t4 = (products[0], products[5] )
# t5 = (products[4], products[1], products[2], products[3] )
# t6 = (products[4], products[1], products[2] )
# t7 = (products[4], products[1] )
# t8 = (products[4], products[5] )
# transactions = sorted([t1,t2,t3,t4,t5,t6,t7,t8])
# print(transactions)

# for item in data.values:
#     for i in range(0,len(item) ):
#         if(str(item[i]) != "nan" and not str(item).startswith('T')):
#             records.append(item[i])
# print(records)
# print(len(records))

# apples = cleanedData.count('Apple')
# print(apples)


import pandas as pd

import apriorLibrary as ap

# Read from file
data = pd.read_csv("marketlist.csv", header=None)
transactions = ap.getTransactions(data)
# print(f'Total transactions: {len(transactions)}')

cleanedData = ap.getCleanData(data)
individualSupports = ap.getIndividualSupport(cleanedData, len(transactions))

for t in transactions:
    print(f"================= {t.tId} Items ================= ")
    print(t.Items)
    print(f"================= {t.tId} Combinations ================= ")
    print(t.Combinations)
