import pyodbc
import streamlit as st
#from azure.identity import AzureCliCredential
#credential = AzureCliCredential()

# Load secrets with error handling
try:
    researchanalyticsapp = st.secrets["researchanalyticsapp"]
except KeyError:
    st.error(f"Error: Could not find secret 'researchanalyticsapp' in Streamlit Cloud.")
    st.stop()  # Stop execution to prevent errors later


queryStr = 'select * from [dbo].[research_publications]' 

#auth = 'ActiveDirectoryInteractive'
#auth = 'ActiveDirectoryPassword'

# Define the SQL Server ODBC connection string

conn_str = (
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={researchanalyticsapp['DATABASE_SERVER']};"
    f"DATABASE={researchanalyticsapp['DATABASE_NAME']};"
    f"UID={researchanalyticsapp['AAD_CLIENT_ID']};"
    f"PWD={researchanalyticsapp['AAD_CLIENT_SECRET']};"
    f"Authentication=ActiveDirectoryServicePrincipal"
)

# Establish the connection
conn = pyodbc.connect(conn_str)


# Execute a query
cursor = conn.cursor()
cursor.execute(queryStr)
resultList = cursor.fetchall()
resultColumns = columns = [column[0] for column in cursor.description]
print(str([dict(zip(columns, row)) for row in resultList]))