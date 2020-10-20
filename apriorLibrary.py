from typing import Counter
import itertools


def getIndividualSupport(dataDictionary, totalTransactions):
    dataDict = Counter(sorted(dataDictionary))
    supportList = []
    for key,value in dataDict.items():
        supportList.append((key, value/totalTransactions))
    return supportList

def getTransactions(data, printData=False):
    transactions = []
    for t in data.values:
        transaction = MarketTransaction(t)
        transactions.append(transaction)
        if(printData):
            print(transaction.tId, transaction.Items)
    return transactions

def getCleanData(data):
    return  [item for sublist in data.values for item in sublist if (str(item) != 'nan' and not str(item).startswith('T'))]

class MarketTransaction:
    def __init__(self, transaction):
        self.tId = transaction[0]
        self.Items = []        
        for i in range(1,len(transaction)):
            if(str(transaction[i]) != 'nan'):
                self.Items.append(transaction[i])
        
        self.Combinations = self.calculateCombinations()

    def calculateCombinations(self):
        combList = []
        for i in range(2,len(self.Items)+1):
            #maybe check out powerset https://stackoverflow.com/questions/464864/how-to-get-all-possible-combinations-of-a-list-s-elements
            comb = itertools.combinations(self.Items, i)
            combList.append(list(comb))
        return combList
