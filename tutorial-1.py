import pandas as pd
import apriorLibrary as ap
from typing import Counter

# Read from file
data = pd.read_csv("marketlist.csv", header=None)


cleanedData = ap.getCleanData(data)
dataDict = Counter(sorted(cleanedData))

individualSupports = ap.getIndividualSupport(cleanedData, len(data.values), threshold=4)
transactionsP1 = ap.getTransactions(data,filteredList=individualSupports)

for t in transactionsP1:
    print(f"================= {t.tId} Items ================= ")
    print(t.Items)
    print(f"================= {t.tId} Combinations ================= ")
    print(t.Combinations)

print("this is a new update")
print("second update")
print("Third update for git tutorial")
