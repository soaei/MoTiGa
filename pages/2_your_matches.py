import streamlit as st
import pandas as pd
import altair as alt
from sklearn import metrics


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
except:
    st.write("Dataframe not found. Please try again on the main page")
    st.stop()

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

try:
    tab_names =  ", ".join(titles)
    tabs = st.tabs(titles)
except:
    st.write("No matches yet. Maybe try a bit harder?")

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


var1 = df['player_1']
var2 = df['player_2']

#conf_matr2
def binary_cm(y_pred_binary, y_test):
    cm = metrics.confusion_matrix(y_test, y_pred_binary, labels=[-1, 1]) 
    cm_df = pd.DataFrame(
        cm,
        index=["Dislike", "Like"],
        columns=["Dislike", "Like"],
    ).reset_index().melt(id_vars="index")
    cm_df.columns = ["Player1", "Player2", "Count"]

    cm_chart = (
        alt.Chart(cm_df)
        .mark_rect()
        .encode(
            x=alt.X(
                "Player2:O",
                title="Player2",
                axis=alt.Axis(labelFontSize=14, titleFontSize=16),
            ),
            y=alt.Y(
                "Player1:O",
                title="Player1",
                axis=alt.Axis(labelFontSize=14, titleFontSize=16),
            ),
            color=alt.Color(
                "Count:Q", legend=alt.Legend(labelFontSize=14, titleFontSize=16)
            ),
            tooltip=["Player1", "Player2", "Count"],
        )
        .properties(
            title=alt.TitleParams(text=" 🤔 Confusion Matrix", fontSize=20),
            width=500,
            height=500,
        )
    )
    threshold = cm_df["Count"].max() / 2.0
    cm_text = cm_chart.mark_text(baseline="middle", fontSize=20).encode(
        text="Count:Q",
        color=alt.condition(
            alt.datum.Count > threshold, alt.value("white"), alt.value("black")
        ),
    )
 # Set color explicitly to black
    cm_text = cm_text.encode(
        color=alt.value("black")
    )
   

    return cm_chart + cm_text

conf_chart = binary_cm(var1, var2)
st.markdown("<h1 style='text-align: left;'>Confusion Matrix</h1>", unsafe_allow_html=True)
st.altair_chart(conf_chart, use_container_width=False)




st.divider()
st.dataframe(show_df)
