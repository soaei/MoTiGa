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
    st.header("Hello there! ")

       #name
    st.text("Please give me a nickname that identifies the game!")
    player_1 = st.text_input("game nick")
    
    player_1_clean = clean_string(player_1)
    if (player_1_clean == player_1) and player_1_clean:        
        con = get_constr(player_1)
        st.session_state[CON_KEY] = con
        st.session_state[PLAYER_COL_KEY] = "player_1"
        o1,oszlop1,o3, oszlop2,o2 =st.columns(5)
        with oszlop1:
            st.markdown("""
            <style>
            .big-font {
                font-size:20px !important;
            }
            </style>
            """, unsafe_allow_html=True)

            st.markdown('<p class="big-font">🎉Joining for the first time</p>', unsafe_allow_html=True)
            
            if st.button("Create new game"):
                    try:
                        # PRIO3: make this more complex
                        # n = st.slider("n", 3, 20, value=6)
                        # n = st.selectbox("n", [3, 10, 20])
                        n = 8
                        filtered_df = df.sample(n)
                        filtered_df.to_sql(TABLE_NAME, con, index=False)
                        st.switch_page("pages\\1_rate_films.py")
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
                    st.switch_page("pages\\1_rate_films.py")
                except (ValueError, OperationalError):
                    st.text("No such game")
        with oszlop2:
            st.write ("")
            st.markdown('<p class="big-font">🎈Rejoin a game  </p>', unsafe_allow_html=True)
            if st.button("Continue game as player 1"):
                st.switch_page("pages\\1_rate_films.py")
            if st.button("Continue game as player 2"):
                st.session_state[PLAYER_COL_KEY] = "player_2"
                st.switch_page("pages\\1_rate_films.py")
            
       

    else:
        st.text("one word, no special characters, all lowercase if you would be so kind!")

