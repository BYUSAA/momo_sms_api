def linear_search(transactions, transaction_id):
    for tx in transactions:
        if tx["id"] == transaction_id:
            return tx
    return None


def dictionary_lookup(transaction_dict, transaction_id):
    return transaction_dict.get(transaction_id)
