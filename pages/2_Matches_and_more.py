import streamlit as st

if "df" in st.session_state:
    df=st.session_state["df"]
    st.dataframe(df)
else:
    st.write("Dataframe not found. Please try again on the main page")