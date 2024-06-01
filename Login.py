import re
from pathlib import Path

import streamlit as st
import pandas as pd

from constants import data_dir, DF_KEY, TABLE_NAME, CON_KEY, PLAYER_COL_KEY

def clean_string(input_string):    
    # Remove special characters and spaces using regular expressions
    return re.sub(r'[^a-z0-9]', '', input_string.lower())


st.set_page_config(
    page_title="Movie Tinder Gangbang ",
    page_icon="🍿",
    layout="wide",
)


if __name__ == "__main__":

    df = pd.read_csv(data_dir / "initial.csv").assign(player_1=0, player_2=0)

    # Add some content to the app
    st.title("Hello there! ")

    st.title ("Start a new game or continue an old one?")

    #name
    st.title("Please give me player 1's nickname, that identifies the game!")
    player_1 = st.text_input("player1 name")

    if st.button("New game"):
        player_1_clean = clean_string(player_1)
        if (player_1_clean == player_1) and player_1_clean:
            con = f"sqlite:///{data_dir.name}/{player_1_clean}.db"
            st.session_state[CON_KEY] = con
            st.session_state[PLAYER_COL_KEY] = "player_1"
            df.to_sql(TABLE_NAME, con)
            st.page_link("pages\\1_Swiping.py")
        else:
            st.text("one word, no special characters, all lowercase if you would be so kind!")

    if st.button("Join as player 2"):
        # TODO: check if given player 1 name is valid
        st.text("player 2 name")
        player_2 = st.text_input("player2 name")
        
    if st.button("Continue game"):
        # TODO: check if given player 1 name is valid
        # TODO: give option to go either player 1 or player 2
        pass
        
    if st.button("See results"):
        # TODO: check if given player 1 name is valid
        # TODO: give option to go either player 1 or player 2
        pass


    st.session_state[DF_KEY]=df.set_index("id")
    st.session_state["player_1"]=player_1
    #st.session_state["player_2"]=player_2
