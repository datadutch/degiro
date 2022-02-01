import json
import pandas as pd
import degiroapi
from degiroapi.product import Product
from degiroapi.order import Order
from degiroapi.utils import pretty_json

def inlog():
    with open('config.json','r') as file:
        data = json.load(file)

def portfolio():
    degiro = degiroapi.DeGiro()
    degiro.login("vanderkooij", "yL34NTq7eNHeXdc4Z")
    portfolio = pd.DataFrame(degiro.getdata(degiroapi.Data.Type.PORTFOLIO, True))
    print(portfolio)
    degiro.logout()

inlog
portfolio