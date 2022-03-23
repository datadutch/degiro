"""Retrieves snowflake credentials from local file."""
import json
import snowflake.connector

with open('c:\git\degiro\config_snowflake.json', 'r') as file:
    data = json.load(file)
    snowflake_user = data['snowflake_user']
    snowflake_password = data['snowflake_password']
    snowflake_account = data['snowflake_account']

ctx = snowflake.connector.connect(
    user=snowflake_user,
    password=snowflake_password,
    account=snowflake_account
    )
cs = ctx.cursor()
try:
    cs.execute("SELECT current_version()")
    one_row = cs.fetchone()
    print(one_row[0])
finally:
    cs.close()
ctx.close()
