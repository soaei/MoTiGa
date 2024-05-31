import streamlit as st
import pandas as pd 
st.set_page_config(
    page_title="Movie Tinder Gangbang ",
    page_icon="🍿",
    layout="wide",
)

# Add some content to the app
st.title("Hello there! ")


st.title ("Start a new game or continue an old one?")
new_or_old = st.radio("", ["Start a new game", "Join existing game", "Continue old one"])


#name
st.title ("Please give me your nickname!")
st.write(" (one word, no special characters, all lowercase if you would be so kind!)")
nickname = st.text_area("",)
st.header(' You have chosen ') 
st.header(nickname)
st.header("Remember it well so you can log in next time!")

#take nickname and make it into the column name format
import re

def clean_string(input_string):
    # Convert the string to lowercase
    lowercased_string = input_string.lower()
    
    # Remove special characters and spaces using regular expressions
    cleaned_string = re.sub(r'[^a-z0-9]', '', lowercased_string)
    
    return cleaned_string

if new_or_old == "Join existing game":
    player_2= 'player2_' + clean_string(nickname) 
else:
    player_1 ='player1_' + clean_string(nickname) 

st.header(player_1)

filepath = "D:\motiga\imdb_adatok.csv"
df =pd.read_csv(filepath)
df[player_1] = None
#df[player_2] = None

st.session_state["df"]=df
