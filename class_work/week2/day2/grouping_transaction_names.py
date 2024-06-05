# For a given array of transactions, group all the transactions by item name. 
# Return an array of strings where each string contains the item name followed 
# by a space and the number of associated transactions. 

# Note: Sort the array descending by transaction count, then ascending by
# alphabetically by item name for items with matching transaction counts. 

# Example: transactions= ['notebook', 'notebook', 'mouse', 'keyboard', 'mouse']

# There are two items with 2 transactions each: 'notebook' and 'mouse'. In 
# alphabetical order, they are 'mouse', 'notebook'. There is 1 item with 1 
# transaction: 'keyboard'. The return array, sorted as required, is 
# ['mouse 2', 'notebook 2', 'keyboard 1'].

# Function Description: Complete the function groupTransactions in the editor below
# group transactions has the following parameter(s): 
# string transactions[n]: each transaction[i] denotes the item name in the ith transaction
# constraints: 1<=n<=10^5, 1<= length of transactions[i] <= 10,
# transactions[i] contains only lowercase English letters ascii[a-z]

def groupTransactions(transactions):
    transactions_map = {}
    for t in transactions:
        transactions_map[t]=transactions_map.get(t, 0)+1

    k=lambda t:(-t[1],t[0])
    result=sorted(transactions_map.items(), key=k)
    
    for i in range(len(result)):
        result[i]=result[i][0]+" "+str(result[i][1])
    
    return result
    

print(groupTransactions(['notebook','notebook','mouse','keyboard','mouse']))
# space O(n), time: O(n*log n)