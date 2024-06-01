import re
from sqlite3 import OperationalError
from pathlib import Path

import streamlit as st
import pandas as pd

from constants import data_dir, TABLE_NAME, CON_KEY, PLAYER_COL_KEY, get_db_file

def clean_string(input_string):    
    # Remove special characters and spaces using regular expressions
    return re.sub(r'[^a-z0-9]', '', input_string.lower())


st.set_page_config(
    page_title="Movie Tinder Gangbang ",
    page_icon="🍿",
    layout="wide",
    initial_sidebar_state="collapsed",
)

def get_constr(player_name):
    return f"sqlite:///{data_dir.name}/{player_name}.db"


if __name__ == "__main__":

    df = pd.read_csv(data_dir / "initial.csv").assign(player_1=0, player_2=0)

    # Add some content to the app
    st.header("🌈 Hello there!  ")

       #name
    st.text("Please give me a nickname that identifies the game!")
    player_1 = st.text_input("game nick")
    
    player_1_clean = clean_string(player_1)
    if (player_1_clean == player_1) and player_1_clean:        
        con = get_constr(player_1)
        db_file = Path(get_db_file(con))
        st.session_state[CON_KEY] = con
        st.session_state[PLAYER_COL_KEY] = "player_1"
        oszlop1,oszlop2 =st.columns(2)
        with oszlop1:
            st.markdown("""
            <style>
            .big-font {
                font-size:20px !important;
            }
            </style>
            """, unsafe_allow_html=True)

            
            if not db_file.exists():
                    st.markdown('<p class="big-font">🎉Joining for the first time</p>', unsafe_allow_html=True)
                    # PRIO3: make this more complex
                    n = st.slider("n", 3, 20, value=6)
                    ratings = df["rating_explanation"].unique()
                    to_select = st.multiselect("Ratings", ratings, default=ratings)
                    if st.button("Start"):
                        filtered_df = df.loc[df["rating_explanation"].isin(to_select), :].sample(n)
                        try:
                            filtered_df.to_sql(TABLE_NAME, con, index=False)
                            st.switch_page("pages\\1_rate_films.py")
                        except ValueError:
                            st.text("game already exists")

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

