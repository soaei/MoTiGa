import streamlit as st
import streamlit.components.v1 as components
import sqlite3
import pandas as pd

from constants import data_dir, TABLE_NAME, CON_KEY, PLAYER_COL_KEY, get_db_file

st.set_page_config(
    page_title="Movie Tinder Gangbang ",
    page_icon="🍿",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.header("Would you like to watch these films?")

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

def get_setter_query(col, val, id_):
    return f"UPDATE {TABLE_NAME} SET {col}={val} WHERE id='{id_}'"

def execue_change(constr, col, val, id_):
    con = sqlite3.connect(get_db_file(constr))
    with con:
        con.execute(get_setter_query(col, val, id_))
    con.close()


if (CON_KEY in st.session_state):
    constr = st.session_state[CON_KEY]
    try:
        df = pd.read_sql(TABLE_NAME, constr).set_index("id")
    except:
        st.text("Not initiated game")
        st.stop()
    col = st.session_state[PLAYER_COL_KEY]
    not_yet_rated = df.loc[df[col] == 0, :]
    if not not_yet_rated.empty:
        id_ = not_yet_rated.index[0]
        #PRIO make this prettier
        title = df.loc[id_, "title"]
        pic_url = df.loc[id_, "img_link"]
        plot = df.loc[id_, "plot"]
        rating = df.loc[id_, "rating"]
        pop = df.loc[id_, "popularity"]
        length = df.loc[id_, "length"]
        year = df.loc[id_, "year"]
        pg = df.loc[id_, "rating_explanation"]
        genre = df.loc[id_, "genre"]

        st.markdown(
            """
        <style>
        button {
            text-align:center;
            height: auto;
            padding-top: 10px !important;
            padding-bottom: 10px !important;
            padding-right: 60px !important;
            padding-left: 60px !important;
        }
        </style>
        """,
            unsafe_allow_html=True,
        )
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image(pic_url, width = 250)
        with col2:
            st.header(title)
            st.write(plot)
            st.write(f'⏰:', length)
            st.write(f'⭐:', rating)
            st.write(f'📈:', pop)
            st.write(f'📆:', year)
            st.write(f'🔞:', pg)
            st.write(f'🎭:', genre)

        with col3:
            if st.button("⚡ Yes ⚡"):
                execue_change(constr, col, 1, id_)
                st.rerun()
            if st.button("Nope"):
                execue_change(constr, col, -1, id_)
                st.rerun()
        
        

                

st.page_link("pages\\2_your_matches.py", label= "ready to see your matches?")
