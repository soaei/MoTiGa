import streamlit.components.v1 as components
import streamlit as st

a=2
if st.button('popup'):

    mycode = "<script>alert('This box is me!' )</script>"
    components.html(mycode, height=0, width=0)