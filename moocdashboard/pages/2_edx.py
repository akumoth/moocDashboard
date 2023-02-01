import streamlit as st
import pandas as pd
import altair as alt
import wordcloud as wc
import matplotlib.pyplot as plt
from datetime import date
import numpy as np
import math

st.title("edX Dashboard - 2017")

edx_df = pd.read_csv("../data/raw/edx_courses.csv")
edx_df['n_enrolled'] = pd.to_numeric(edx_df['n_enrolled'].str.replace(',', ''))
edx_df['price'] = pd.to_numeric(edx_df['price'].str.replace('[^0-9]',''))
edx_df['course_length'] = pd.to_numeric(edx_df['course_length'].str.replace('[^0-9]',''))
edx_df['course_effort'] = edx_df['course_effort'].str.replace(' hours per week','')
edx_df['course_effort'] = edx_df['course_effort'].astype(str)
edx_df['course_effort'] = edx_df['course_effort'].str.split('–')
edx_df['course_effort'] = edx_df['course_effort'].apply(lambda x: int(x[0]) + (int(x[0]) / int(x[1])))

filter1, filter2, filter3 = st.sidebar.columns(3)
with filter1:
    topicfilter = st.checkbox("Filtro según topico")
with filter2:
    levelfilter = st.checkbox("Filtro según nivel")
with filter3:
    langfilter = st.checkbox("Filtro según idioma")

subject = st.sidebar.selectbox(
    "Topico de la vista actual",
    (edx_df.subject.unique())
)
level = st.sidebar.selectbox(
    "Nivel educativo de la vista actual",
    (edx_df.Level.unique())
)
language = st.sidebar.selectbox(
    "Lenguaje seleccionado en la vista actual",
    (edx_df.language.unique())
)
    
var1, var2 = st.sidebar.columns(2)
with var1:
    linechartx = st.selectbox(
        '''Variable del gráfico de lineas''',
        ('price','course_length','course_effort')
    )
with var2:
    piechartx = st.selectbox(
        "Categoría del gráfico de torta",
        ('course_type','language','Level','subject')
    )

current_view = edx_df.drop(edx_df.sort_values(by='price',ascending=False)['price'].head(8).index)

if topicfilter == True:
    current_view = current_view[current_view.subject == subject]
if levelfilter == True:
    current_view = current_view[current_view.Level == level]
if langfilter == True:
    current_view = current_view[current_view.language == language]


umetric1, umetric2, umetric3 = st.columns(3)
profits = ("{:,}".format(math.floor(((current_view.price * current_view.n_enrolled).sum())/100000))) + "M"
subsnum = "{:,}".format(math.floor((current_view.n_enrolled.sum())/100000)) + "M"
with umetric1:
    st.metric("Estimado de las ganancias totales:", value=(profits))
with umetric2:
    st.metric("Numero de inscripciones:", value=(subsnum))
with umetric3:
    st.metric("Numero de cursos:", current_view.title.value_counts().sum())

st.dataframe(current_view[['title','n_enrolled']].sort_values(by='n_enrolled',ascending=False).head(10))

lchart, pchart = st.columns(2)
with lchart:
    st.line_chart(current_view,y="n_enrolled",x=linechartx)
with pchart:
    subjectchart = alt.Chart(current_view).mark_arc(innerRadius=50).encode(
        theta=alt.Theta(field="n_enrolled", type="quantitative"),
        color=alt.Color(field=piechartx, type="nominal"),
    )
    st.altair_chart(subjectchart.interactive(), use_container_width=True)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
titles = " ".join(i for i in current_view.title)
stopwords = set(wc.STOPWORDS)
mywc = wc.WordCloud(width=1280,height=720,stopwords=stopwords, background_color="white").generate(titles)
ax.imshow(mywc, interpolation='bilinear')
ax.axis("off")
st.pyplot(fig)