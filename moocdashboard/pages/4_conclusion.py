import streamlit as st
import pandas as pd

st.markdown(
    '''
    * Los cursos con mayor KPI a lo largo de las distintas disciplinas son siempre aquellos destinados a principiantes\n
    * Sin embargo, vemos que la ganancia promedia por venta de curso aumenta bastante en los cursos destinados 
    a personas con conocimiento intermedio o experto\n
    * En orden de mayor KPI a menos KPI en los cursos de Udemy, tenemos las siguientes disciplinas: Web Development, 
    Graphic Design, Business Finance, y Musical Instruments. Sin embargo, a pesar de su exito, los cursos de Graphic 
    Design toman un espacio bastante reducido de los cursos presentes en la plataforma.
    * Además de esto, en los cursos de Graphic Design hay más gente dispuesta a pagar que en los demás, particularmente 
    en cursos principiantes (lo opuesto es cierto para las demás categorias), por lo que intuimos que es un area del 
    mercado en la que vale la pena invertir.

    * En edX, vemos que la mayoría de los cursos de comunicación (principalmente certificaciones para el conocimiento de 
    ciertos lenguajes) y analísis de datos disfrutan de bastante estudiantes inscritos también, generalmente siendo la misma
    cantidad inclusos en cursos con un precio de certificación mayor a 0
    * Los cursos de CS50 son los más populares en la plataforma, pero si los descontamos, vemos que dentro del top 10 de
    cursos más inscritos tenemos una variedad saludable de topicos
    * En el idioma español, hay mucha demanda en cursos en los que se podría esperar obtener un trabajo a distancia 
    después de la certificación: cursos de marketing digital, informatica, Excel, y analísis de datos.
    '''
)