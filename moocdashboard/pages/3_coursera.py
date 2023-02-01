import streamlit as st
import pandas as pd
import altair as alt
import wordcloud as wc
import matplotlib.pyplot as plt
from datetime import date
import numpy as np
import math

st.title("Coursera Dashboard - 2017")

coursera_df = pd.read_parquet("../data/processed/coursera_cnr.parquet")
current_view = coursera_df

umetric1, umetric2 = st.columns(2)
profits = ("{:,}".format(math.floor(((current_view.rating_count).sum())/100000))) + "M"
with umetric1:
    st.metric("Reseñas totales:", value=(profits))
with umetric2:
    st.metric("Numero de cursos:", current_view.name.value_counts().sum())

dfview1, dfview2 = st.columns(2)
with dfview1:
    st.dataframe(current_view[['name','rating_count']].sort_values(by='rating_count',ascending=False).head(10))
with dfview2:
    st.dataframe(current_view[current_view.rating_count > 1000][['name','average_rating']].sort_values(by='average_rating',ascending=False).head(10))

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
titles = " ".join(i for i in current_view.name)
stopwords = set(wc.STOPWORDS)
mywc = wc.WordCloud(width=1280,height=720,stopwords=stopwords, background_color="white").generate(titles)
ax.imshow(mywc, interpolation='bilinear')
ax.axis("off")
st.pyplot(fig)