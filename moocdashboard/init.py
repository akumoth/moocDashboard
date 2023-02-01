import streamlit as st
import pandas as pd

st.title("Introducción")

st.image("../_src/D430_50_073_1200.jpg")

st.markdown(
    '''
    Entrar actualmente al mercado de los MOOCs es díficil. 
    Existe un numero reducido de empresas que abarcan porciones bastante grandes de este mercado, 
    no solamente mediante la oferta de una gran cantidad de cursos, sino también colaborando con universidades 
    e institutos alrededor del mundo que buscan entregar su educación en una modalidad online. El atractivo 
    que presenta el poder recibir una educación formal (y un certificado, cuando se tenga el dinero necesario) 
    de una institución prestigiosa desde cualquier parte del mundo es incuestionable, y aquellos que 
    pueden proveer esta certificación terminan atrayendo un alto numero de clientes. Además, estas empresas ya actualmente 
    ofrecen en ciertas disciplinas un gran numero de recursos populares que atraen más y más novatos cada día.\n

    Por estas y otras razones, es importante para cualquier competidor nuevo en este mercado no solamente analizar
    los productos y las tendencias más exitosas, sino también ser capaz de identificar la posible demanda de cursos en
    mercados sin explotar, nichos sin descubrir, o disciplinas nuevas con pocos recursos existentes, para poder encontrar
    un area del mercado en la cual crecer y encontrar una audiencia cautiva. A cuales temas, herramientas o profesiones se les 
    debería prestar atención, y como deberían presentarse estos cursos? Que duración deberían tener, en que lenguaje se deberían 
    realizar, a que niveles de educación se les debería apuntar? Son preguntas que se deben hacer y responder con claridad, 
    sin dejar lugar a la improvisación, utilizando datos y analisis reales de la situación actual.\n

    Con esto en mente, hemos diseñado 3 dashboards donde nuestra PM podrá encontrar datos de 3 empresas de MOOCs que disfrutan 
    de gran popularidad actualmente: edX, Udemy y Coursera. En estos, se podrá ver de forma clara datos que revelan cuales cursos
    en estas plataformas reciben la mayor atención, y a cuales categorias pertenecen. En el desarrollo de estos dashboards, 
    nos hemos enfocado en Udemy por la calidad y completitud de los datos, y como resultado, es en el cual hemos basado 
    nuestro KPI:
    '''
)

st.latex(r"\frac{\frac{(precio * suscriptores)}{meses}}{duración del contenido}")

st.markdown(
    '''
    Este KPI lo escogimos en función de explorar cuales cursos eran los que ofrecian la mayor ganancia con la menor inversión
    de recursos en video posible: al multiplicar el precio por los suscriptores, obtenemos la ganancia total del curso, y 
    al dividir esta ganancia entre los meses, tenemos la ganancia promedio por cada mes. Este numero después lo dividimos entre 
    la duración total del contenido creado para el curso (dado en horas) y tenemos como resultado una metrica de cual es la 
    ganancia promedio por hora del curso.\n

    En estos dashboards, nuestra PM podrá realizar un analisis comparativo no solamente entre las distintas empresas, sino también
    entre distintos topicos de cursos, fechas de salida, y niveles de curso.
    '''
)