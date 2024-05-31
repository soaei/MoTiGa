import streamlit as st
import pandas as pd 
st.set_page_config(
    page_title="Movie Tinder Gangbang ",
    page_icon="🍿",
    layout="wide",
)

# Add some content to the app
st.title("Hello there! ")

#get df
filepath = "D:\motiga\kisminta.csv"
df =pd.read_csv(filepath)

st.title ("Start a new game or continue an old one?")
new_or_old = st.radio("", ["New game", "Existing game", "Rejoin"])


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


column_name_1 ='player1_' + clean_string(nickname) 
column_name_2 ='player2_' + clean_string(nickname)

##Establishing players in new game
if new_or_old == "New game":
    player_1 ='player1_' + clean_string(nickname) 
    df.rename(columns={'player_1' :player_1}, inplace = True)
elif new_or_old == "Existing game":
    player_2 ='player_2' + clean_string(nickname) 
    df.rename(columns={'player_2 ' :player_2}, inplace = True)

##Reentering players
 

if new_or_old == "Rejoin":
    if column_name_1 in df.columns:
        st.text( "Welcome back "+ nickname)
        player_1 = 'player1_' + clean_string(nickname)  
    elif column_name_2 in df.columns:
        st.text( "Welcome back "+ nickname)
        player_2 = 'player2_' + clean_string(nickname) 
    else:
        st.write("There is no such player found, please try again. If you have not yet played, please try joining a game")


st.page_link("pages\\1_Swiping.py")

st.header(player_1)



st.session_state["df"]=df

st.session_state["player_1"]=player_1
st.session_state["player_2"]=player_2
