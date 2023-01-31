import streamlit as st
import pandas as pd
import altair as alt
import wordcloud as wc
import matplotlib.pyplot as plt
from datetime import date
import numpy as np

st.title("Udemy Dashboard - 2017")
udemy_df = pd.read_csv("../data/raw/udemy_courses.csv")
udemy_df.published_timestamp = udemy_df.apply(lambda x: x['published_timestamp'][:-10],axis=1)
udemy_df.published_timestamp = pd.to_datetime(udemy_df.published_timestamp)
udemy_df = udemy_df.assign(kpi=(udemy_df.price * udemy_df.num_subscribers)/((abs((udemy_df.published_timestamp - pd.to_datetime('2018-01-01'))/np.timedelta64(1,'M')))/udemy_df.content_duration))

year_month = st.sidebar.slider(
    "Rango de tiempo",
    udemy_df.published_timestamp.min(),
    udemy_df.published_timestamp.max(),
    (date(2011,7,9),
    date(2017,7,6)
    )
)

filter1, filter2 = st.sidebar.columns(2)
with filter1:
    topicfilter = st.checkbox("Habilitar filtro según topico")
with filter2:
    levelfilter = st.checkbox("Habilitar filtro según nivel")

option1, option2 = st.sidebar.columns(2)
with option1:
    subject = st.selectbox(
        "Topico de la vista actual",
        (udemy_df.subject.unique())
    )
with option2:
    level = st.selectbox(
        "Nivel educativo de la vista actual",
        (udemy_df.level.unique())
    )

var1, var2 = st.sidebar.columns(2)
with var1:
    linechartx = st.selectbox(
        '''Variable del gráfico de lineas''',
        ('price','num_lectures','content_duration','num_reviews')
    )
with var2:
    piechartx = st.selectbox(
        "Categoría del gráfico de torta",
        ('subject','level','is_paid')
    )

current_view = (
    udemy_df[
        (udemy_df.published_timestamp > pd.to_datetime(year_month[0])) & 
        (udemy_df.published_timestamp < pd.to_datetime(year_month[1]))]
    )
if topicfilter == True:
    current_view = current_view[current_view.subject == subject]
if levelfilter == True:
    current_view = current_view[current_view.level == level]

umetric1, umetric2, umetric3 = st.columns(3)
profits = str((current_view.price * current_view.num_subscribers).sum())
subsnum = str(current_view.num_subscribers.sum())
with umetric1:
    st.metric("Estimado de las ganancias totales:", value=(profits[:3] + 'K$'))
with umetric2:
    st.metric("Usuarios totales:", value=(profits[:3] + 'K'))
with umetric3:
    st.metric("Numero de cursos:", current_view.course_title.value_counts().sum())

st.dataframe(current_view[['course_title','kpi']].sort_values(by='kpi',ascending=False).head(5))

lchart, pchart = st.columns(2)
with lchart:
    st.line_chart(current_view,y="num_subscribers",x=linechartx)
with pchart:
    subjectchart = alt.Chart(current_view).mark_arc(innerRadius=50).encode(
        theta=alt.Theta(field="num_subscribers", type="quantitative"),
        color=alt.Color(field=piechartx, type="nominal"),
    )
    st.altair_chart(subjectchart, use_container_width=True)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
titles = " ".join(i for i in current_view.course_title)
stopwords = set(wc.STOPWORDS)
mywc = wc.WordCloud(width=1280,height=720,stopwords=stopwords, background_color="white").generate(titles)
ax.imshow(mywc, interpolation='bilinear')
ax.axis("off")
st.pyplot(fig)