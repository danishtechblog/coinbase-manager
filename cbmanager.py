#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#       +----------------------------------------------------+
#       | Title: Coinbase Manager v1.0                       |
#       | Web: https://danish.tech                           |
#       | Support: https://forum.danish.tech                 |
#       +----------------------------------------------------+
#
#       Instructions:
#       - pip install coinbase
#       - add your api key in the api_key variable
#       - add your api secretin the api_secret variable


from coinbase.wallet.client import Client
import os

os.system("clear")

api_key = ""        # insert your api key here
api_secret = ""     # insert your api secret here

client = Client(api_key, api_secret)
time = client.get_time().iso
user = client.get_current_user()
balance = client.get_primary_account().balance

print("+------------------------------------------------+")
print("| Coinbase Bitcoin Manager v1.0                  |")
print("+------------------------------------------------+")
print
print("Server time: %s " % time)
print("Name: %s " % user.name)
print("Primary Wallet Balance: %s " % balance)
print("--------------------------------------------------")
buy = client.get_buy_price(currency_pair = 'BTC-USD')
print("BTC Buy Price: %s " % buy)
sale = client.get_sell_price(currency_pair = 'BTC-USD')
print("BTC Sales Price: %s " % sale)
print("--------------------------------------------------")
