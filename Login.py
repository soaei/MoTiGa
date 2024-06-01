import re
from sqlite3 import OperationalError
from pathlib import Path

import streamlit as st
import pandas as pd

from constants import data_dir, TABLE_NAME, CON_KEY, PLAYER_COL_KEY

def clean_string(input_string):    
    # Remove special characters and spaces using regular expressions
    return re.sub(r'[^a-z0-9]', '', input_string.lower())


st.set_page_config(
    page_title="Movie Tinder Gangbang ",
    page_icon="🍿",
    layout="wide",
)

def get_constr(player_name):
    return f"sqlite:///{data_dir.name}/{player_name}.db"

if __name__ == "__main__":

    df = pd.read_csv(data_dir / "initial.csv").assign(player_1=0, player_2=0)

    # Add some content to the app
    st.title("Hello there! ")
    st.title ("Start a new game or continue an old one?")

    #name
    st.title("Please give me player 1's nickname, that identifies the game!")
    player_1 = st.text_input("player1 name")

    player_1_clean = clean_string(player_1)
    if (player_1_clean == player_1) and player_1_clean:        
        con = get_constr(player_1)
        st.session_state[CON_KEY] = con
        st.session_state[PLAYER_COL_KEY] = "player_1"
        if st.button("New game"):
                try:
                    df.sample(6).to_sql(TABLE_NAME, con, index=False)
                    st.switch_page("pages\\1_Swiping.py")
                except ValueError:
                    st.text("game already exists")

        if st.button("Join as player 2"):
            st.text("player 2 name")
            player_2 = st.text_input("player2 name")
            col = "player_2"
            con = get_constr(player_1)
            try:
                df = pd.read_sql(TABLE_NAME, con)
                n = (df[col] == 0).sum()
                st.text(f"{n} remains to rate")
                st.session_state[PLAYER_COL_KEY] = col
                st.session_state[CON_KEY] = con
                st.switch_page("pages\\1_Swiping.py")
            except (ValueError, OperationalError):
                st.text("No such game")
            
        if st.button("Continue game as player 1"):
            st.switch_page("pages\\1_Swiping.py")
        if st.button("Continue game as player 2"):
            st.session_state[PLAYER_COL_KEY] = "player_2"
            st.switch_page("pages\\1_Swiping.py")
            
        st.page_link("pages\\2_Matches_and_more.py", label="See Results")

    else:
        st.text("one word, no special characters, all lowercase if you would be so kind!")

