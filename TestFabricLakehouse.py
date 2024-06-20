import pyodbc

# Some other example server values are

# server = 'localhost\sqlexpress' # for a named instance

# server = 'myserver,port' # to specify an alternate port

server = '5gioeyiqk2putm2fvq5sqbp74q-ugk5yddp5cde7dwlcg6pyljihy.datawarehouse.fabric.microsoft.com'

database = 'PA_Lakehouse'

username = 'ankurarora@perceptanalytics.com'

table = 'research_publications'

auth = 'ActiveDirectoryInteractive'

# ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Authentication='+auth+';UID='+username+';ENCRYPT=yes')

cursor = cnxn.cursor()

 

# Sample select query

cursor.execute("SELECT * FROM "+table)

row = cursor.fetchone()

for row in cursor:
    print("|".join(map(str, row)))  # Convert each element to string and join with "|"

'''
while row:

    print(str(row[0])+'|'+str(row[1]))

    row = cursor.fetchone()
'''