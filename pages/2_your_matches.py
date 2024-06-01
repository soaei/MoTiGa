import streamlit as st
import pandas as pd
from sklearn import metrics

from constants import CON_KEY, TABLE_NAME

try:
    con = st.session_state[CON_KEY]
    #PRIO1 make this pretty
    df = pd.read_sql(TABLE_NAME, con)
    df = df.assign(s=lambda df: df.loc[:, ["player_1", "player_2"]].sum(axis=1)).sort_values("s", ascending=False)
    match_df = (df[df["s"] == 2])

    st.dataframe(match_df)

    p1 = df["player_1"]
    p2 = df["player_2"]

    confusion_matrix = metrics.confusion_matrix(p1, p2)
    st.write("Confusion Matrix:")
    st.write(confusion_matrix)

except:
    st.write("Dataframe not found. Please try again on the main page")