# De Giro & PowerBI
De Giro API calls using Python (it uses https://github.com/lolokraus/DegiroAPI)

If you want to login using the python script, you need to disable MFA

If you do not disable MFA, the error message will be: Exception: Could not login. Response: {"status":6,"statusText":"totpNeeded"}

If you use the wrong credentials, the error message will be: Exception: Could not login. Response: {"status":3,"statusText":"badCredentials"}

Prerequisites:

Python installed, preferrably creating a virtual environment where you have to install some stuff (well documented on the [Microsoft site] (https://docs.microsoft.com/en-us/power-bi/connect-data/desktop-python-scripts) -> this site does not mention the virtual environment but it is higly recommended.
Do not forget to start your virtual environment and point Powerbi (Options, Python scripting)

Watch this video from Koos van Strien about [installing Python] (https://www.youtube.com/watch?v=XA6M_9Gf_yM) for use in Powerbi 

Current status:

the script works when doing a copy paste of the python code into the Powerbi - get data - python screen. Make sure to adjust the path to your local git path and to create a file called config.json with your de Giro credentials

Open Powerbi, Get data, Python -> then copy the script /Users/johanvanderkooij/git/degiro/call_portfolio_no_function.py into the Powerbi screen

Press OK

Select dataset Python - portfolio and there you go

To-do:

Creating a function (currently in feature branch development)

Call the script from Powerbi instead of copy the code (currently stuck on vague indentation errors)

Create code snippets for the other API calls (products, transactions, account)

Also: take a look at yet another Koos video about how to pick up the stock details using Python: (https://www.youtube.com/watch?v=Gc3MugGpIhY)


Executing code from scripts in PowerBI: https://blog.crossjoin.co.uk/2014/02/04/loading-power-query-m-code-from-text-files/
https://community.powerbi.com/t5/Desktop/Can-I-run-external-Python-scripts-in-Power-BI-desktop/m-p/2084822#M775602
