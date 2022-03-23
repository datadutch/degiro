import snowflake.connector
import json
from datetime import datetime
import pandas as pd
import degiroapi
from degiroapi.product import Product
from degiroapi.order import Order
from degiroapi.utils import pretty_json

with open('..\config_snowflake.json','r') as file:
    data = json.load(file)
    user = data['snowflake_user']
    password = data['snowflake_password']
    account = data['snowflake_account']
    
# Gets the version
ctx = snowflake.connector.connect(
    user='<user>',
    password='<password>',
    account='<account>'
    )
cs = ctx.cursor()
try:
    cs.execute("SELECT current_version()")
    one_row = cs.fetchone()
    print(one_row[0])
finally:
    cs.close()
ctx.close()