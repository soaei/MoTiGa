import streamlit as st
import streamlit.components.v1 as components
import sqlite3
import random

from constants import data_dir, DF_KEY, TABLE_NAME, CON_KEY, PLAYER_COL_KEY

st.title("Swiper Cards with Streamlit")

# Define the HTML and JavaScript code
html_code = """
<!DOCTYPE html>
<html>
<head>
    <title>Swiper Cards Example</title>
    <link rel="stylesheet" href="https://unpkg.com/swiper/swiper-bundle.min.css" />
    <style>
        .swiper-container {
            width: 100%;
            max-width: 600px;
            height: 400px;
            margin: 0 auto;
        }
        .swiper-slide {
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 22px;
            color: #fff;
            background-color: #007aff;
        }
        .swiper-slide img {
            width: 100%;
            height: auto;
        }
    </style>
</head>
<body>
    <div class="swiper-container">
        <div class="swiper-wrapper">
            <div class="swiper-slide">
                <img src="images/image1.jpg" alt="Image 1">
            </div>
            <div class="swiper-slide">
                <img src="images/image2.jpg" alt="Image 2">
            </div>
            <div class="swiper-slide">
                <img src="images/image3.jpg" alt="Image 3">
            </div>
        </div>
        <!-- Add Pagination -->
        <div class="swiper-pagination"></div>
        <!-- Add Navigation -->
        <div class="swiper-button-next"></div>
        <div class="swiper-button-prev"></div>
    </div>
    <script src="https://unpkg.com/swiper/swiper-bundle.min.js"></script>
    <script>
        var swiper = new Swiper('.swiper-container', {
            pagination: {
                el: '.swiper-pagination',
            },
            navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev',
            },
        });
    </script>
</body>
</html>
"""

# Embed the HTML and JavaScript code in Streamlit
# components.html(html_code, height=600)

def get_query(col, val, id_):
    return f"""UPDATE {TABLE_NAME}
SET {col} = {val}
WHERE
    id='{id_}'"""

if ("df" in st.session_state) and (CON_KEY in st.session_state):
    df = st.session_state[DF_KEY]
    constr = st.session_state[CON_KEY]
    col = st.session_state[PLAYER_COL_KEY]
    not_yet_rated = df.loc[df[col] == 0, :]

    if not not_yet_rated.empty:
        id_ = random.choice(not_yet_rated.index)
        st.text(df.loc[id_, "title"])
        for word, val in [("Like", 1), ("Dislike", -1)]:
            if st.button(word, f"{word}-{id_}"):
                con = sqlite3.connect(constr.replace("sqlite:///", ""))
                cur = con.cursor()
                cur.execute(get_query(col, val, id_))
                con.commit()
                cur.close()
                cur.close()
                st.text(f"{word}d {id_}")

st.page_link("pages\\2_Matches_and_more.py", label= "ready to see your matches?")
