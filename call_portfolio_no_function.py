<<<<<<< HEAD
import sqlite3
con = sqlite3.connect('degiro.db')

import json
import pandas as pd
import degiroapi
from degiroapi.product import Product
from degiroapi.order import Order
from degiroapi.utils import pretty_json

with open('c:\git\degiro\config.json','r') as file:
    data = json.load(file)
    user = data['degiro_user']
    password  = data['degiro_password']

degiro = degiroapi.DeGiro()
degiro.login(user, password)
portfolio = pd.DataFrame(degiro.getdata(degiroapi.Data.Type.PORTFOLIO, False))

tickerinfo = portfolio.apply(lambda row : degiro.product_info(row['id']), axis = 1, result_type = 'expand')

portfolio[tickerinfo.columns] = tickerinfo

del(tickerinfo)
degiro.logout()
=======
mport sqlite3#(lf)con = sqlite3.connect('degiro.db')#(lf)#(lf)import json#(lf)import pandas as pd#(lf)import degiroapi#(lf)from degiroapi.product import Product#(lf)from degiroapi.order import Order#(lf)from degiroapi.utils import pretty_json#(lf)#(lf)with open('c:\git\degiro\config.json','r') as file:#(lf)    data = json.load(file)#(lf)    user = data['degiro_user']#(lf)    password  = data['degiro_password']#(lf)#(lf)degiro = degiroapi.DeGiro()#(lf)degiro.login(user, password)#(lf)portfolio = pd.DataFrame(degiro.getdata(degiroapi.Data.Type.PORTFOLIO, False))#(lf)#(lf)tickerinfo = portfolio.apply(lambda row : degiro.product_info(row['id']), axis = 1, result_type = 'expand')#(lf)#(lf)portfolio[tickerinfo.columns] = tickerinfo#(lf)#(lf)del(tickerinfo)#(lf)degiro.logout()"),
    portfolio1 = Source{[Name="portfolio"]}[Value],
>>>>>>> cec6454 (updates)
