import pandas as pd
import apriorLibrary as ap
from typing import Counter

# Read from file
data = pd.read_csv("marketlist.csv", header=None)
transactionsP1 = ap.getTransactions(data)

cleanedData = ap.getCleanData(data)
dataDict = Counter(sorted(cleanedData))

individualSupports = ap.getIndividualSupport(cleanedData, len(data.values), threshold=4)


for t in transactionsP1:
    print(f"================= {t.tId} Items ================= ")
    print(t.Items)
    print(f"================= {t.tId} Combinations ================= ")
    print(t.Combinations)
