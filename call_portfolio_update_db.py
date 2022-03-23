import sqlite3
conn = sqlite3.connect('degiro.db')
c = conn.cursor()

import json
from datetime import datetime
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

# c.execute('DROP TABLE IF EXISTS portfolio')
c.execute('CREATE TABLE IF NOT EXISTS portfolio (datum text, name text, value real)')
conn.commit()

db_update = pd.DataFrame(portfolio, columns= ['category','name','value'])

ts = datetime.now().strftime
# ts = '2020-1-31'.strftime

print(ts)


# print(db_update)

db_update.to_sql('portfolio', conn, if_exists='replace', index = False)

# c.execute('''UPDATE portfolio SET category = (?)''',(ts,))


del(tickerinfo)
degiro.logout()