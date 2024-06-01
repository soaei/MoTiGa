import streamlit as st
import pandas as pd

from constants import CON_KEY, TABLE_NAME

try:
    con = st.session_state[CON_KEY]
    #PRIO1 make this pretty
    df = pd.read_sql(TABLE_NAME, con)
    st.dataframe(df.assign(s=lambda df: df.loc[:, ["player_1", "player_2"]].sum(axis=1)).sort_values("s", ascending=False))

except:
    st.write("Dataframe not found. Please try again on the main page")