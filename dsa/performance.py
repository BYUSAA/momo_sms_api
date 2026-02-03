import json
import time
from dsa.search import linear_search, dictionary_lookup

with open("data/transactions.json") as f:
    transactions = json.load(f)

transaction_dict = {tx["id"]: tx for tx in transactions}
target_id = transactions[-1]["id"]

start = time.time()
linear_search(transactions, target_id)
linear_time = time.time() - start

start = time.time()
dictionary_lookup(transaction_dict, target_id)
dict_time = time.time() - start

print("Linear Search Time:", linear_time)
print("Dictionary Lookup Time:", dict_time)
