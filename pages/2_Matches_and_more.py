import streamlit as st
import pandas as pd

from constants import CON_KEY, TABLE_NAME

try:
    con = st.session_state[CON_KEY]
    df = pd.read_sql(TABLE_NAME, con)
    st.dataframe(df)
except:
    st.write("Dataframe not found. Please try again on the main page")