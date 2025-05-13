import streamlit as st
import pandas as pd
from supabase import create_client, Client

# Initialize connection to db
@st.cache_resource
def init_connection():
    url: str = st.secrets['supabase_url']
    key: str = st.secrets['supabase_key']

    client: Client = create_client(url,key)

    return client

supabase = init_connection()


# Query the db

def run_query():
    result = supabase.table('car_parts_monthly_sales').select("*").eq('parts_id',2674).execute()
    df = pd.DataFrame(result.data)
    return df

    #Filter data with eq attribute



st.title("Query a database")

rows = run_query()

df = run_query()
#Store in df

st.write(df)