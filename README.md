# degiro
De Giro API calls using Python

If you want to login using the python script, you need to disable MFA

If you do not disable MFA, the error message will be: Exception: Could not login. Response: {"status":6,"statusText":"totpNeeded"}

If you use the wrong credentials, the error message will be: Exception: Could not login. Response: {"status":3,"statusText":"badCredentials"}
