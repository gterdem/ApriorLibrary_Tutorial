import pandas as pd
import apriorLibrary as ap

# Read from file
data = pd.read_csv("marketlist.csv", header=None)
transactions = ap.getTransactions(data)

cleanedData = ap.getCleanData(data)
individualSupports = ap.getIndividualSupport(cleanedData, len(transactions))

for t in transactions:
    print(f"================= {t.tId} Items ================= ")
    print(t.Items)
    print(f"================= {t.tId} Combinations ================= ")
    print(t.Combinations)
