import pyodbc
import streamlit as st
import pandas as pd

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

# Fetch Data
df = pd.read_sql(queryStr, conn)

# Streamlit App
st.title(" Dashboard - Research Anaytics")

# Section 1: Streamlit Built-in Tables
st.header("Research Publications - Lookup")
st.dataframe(df,use_container_width=True,hide_index=True)  # Interactive DataFrame

#st.header("2. Streamlit `st.table`")
#st.table(df)  # Static Table