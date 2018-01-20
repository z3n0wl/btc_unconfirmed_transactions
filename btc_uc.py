#!/usr/bin/env python

import requests
import sys
from bs4 import BeautifulSoup

def check_unconfirmed_transactions():
    unconfirmed_transaction_url = "https://blockchain.info/unconfirmed-transactions"
    resp = requests.get(unconfirmed_transaction_url)
    unconfirmed_transaction_soup = BeautifulSoup(resp.text, 'html.parser')
    container = unconfirmed_transaction_soup.find(class_='container')
    if(container):
        transactions = container.find(id='header')
        if(len(transactions)>0):
            unconfirmed_transaction = transactions.contents[0].replace(" Unconfirmed Transactions", "")
            return unconfirmed_transaction
        else:
            print("Error during page parsing")
    else:
        print("Error")

print("Bitcoin Unconfirmed Transaction is running on " + sys.platform)
unconfirmed_transaction = check_unconfirmed_transactions()
print(unconfirmed_transaction + " Unconfirmed Bitcoin Transactions")
