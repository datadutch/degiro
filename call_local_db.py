import sqlite3
conn = sqlite3.connect('degiro_new.db')
c = conn.cursor()

import json
from datetime import datetime
import pandas as pd
import degiroapi
from degiroapi.product import Product
from degiroapi.order import Order
from degiroapi.utils import pretty_json


# c.execute('''UPDATE portfolio SET category = (?)''',(ts,))

c.execute('''  
SELECT * FROM portfolio
          ''')

for row in c.fetchall():
    print (row)
    
