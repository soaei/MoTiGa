import streamlit as st

st.set_page_config(
    page_title="Movie Tinder Gangbang ",
    page_icon="🍿",
    layout="wide",
)

new_pins = [1,2,3,4,5,6,7,8,9]
taken_pins = [10,11,12,13]

# Add some content to the app
st.title("Hello there! ")

#pin
st.title ("Start a new game or continue an old one?")
new_or_old = st.radio("", ["Start a new game", "Continue old one"])

if new_or_old == "Start a new game":
    pin = st.selectbox("",new_pins),
else:
    pin = st.selectbox("", taken_pins)




#name
st.title ("Please give me your nickname! (one word, no special characters, all lowercase if you would be so kind!)")
nickname = st.text_area("",)
st.header(' You have chosen ') 
st.header(nickname)
st.header("Remember it well so you can log in next time!")