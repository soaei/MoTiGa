import streamlit as st
import pandas as pd
#from sklearn.metrics import metrics

from constants import CON_KEY, TABLE_NAME
st.set_page_config(
    page_title="Movie Tinder Gangbang ",
    page_icon="🍿",
    layout="wide",
    initial_sidebar_state="collapsed",
)


try:
    con = st.session_state[CON_KEY]
    #PRIO1 make this pretty
    df = pd.read_sql(TABLE_NAME, con)
    df = df.assign(s=lambda df: df.loc[:, ["player_1", "player_2"]].sum(axis=1)).sort_values("s", ascending=False)
    match_df = (df[df["s"] == 2])
    show_columns = ["title", "rating", "length", "popularity", "genre"]
    show_df = match_df[show_columns]


    st.title("🔥Here are you matches!")
    
    
    match_number = match_df.shape[0]
    col0, col1, col2 = st.columns(3)
    image_links = match_df["img_link"].tolist()
    plots = match_df["plot"].tolist()
    titles = match_df["title"].tolist()
    ratings = match_df["rating"].tolist()
    pop = match_df["popularity"].tolist()
    length = match_df["length"].tolist()
    year = match_df["year"].tolist()
    pg = match_df["rating_explanation"].tolist()
    genre = match_df["genre"].tolist()
   
   
    tab_names =  ", ".join(titles)
    tabs = st.tabs(titles)

    tab_counter = 0
    for i, tab in enumerate(tabs):

        with tab:
            col1, col2 = st.columns(2)
            with col1:
                st.image(image_links[i], width=250)
            with col2:
                st.subheader(titles[i])
                st.write (plots[i])
                st.write(f'⏰:', length[i])
                st.write(f'⭐:', ratings[i])
                st.write(f'📈:', pop[i])
                st.write(f'📆:', year[i])
                st.write(f'🔞:', pg[i])
                st.write(f'🎭:', genre[i])
    st.divider()
    st.divider()
    st.dataframe(show_df)
except:
    st.write("Dataframe not found. Please try again on the main page")