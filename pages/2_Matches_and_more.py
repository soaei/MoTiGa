import streamlit as st
import pandas as pd

from constants import CON_KEY, TABLE_NAME

if CON_KEY in st.session_state:
    con = st.session_state[CON_KEY]
    df = pd.read_sql(TABLE_NAME, con)
    st.dataframe(df)
else:
    st.write("Dataframe not found. Please try again on the main page")