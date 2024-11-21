import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header('Cuadro de Mandos: Análisis de Vehículos')

# Botones para visualizaciones
if st.button('Mostrar Histograma del Odometer'):
    st.write('Histograma: Distribución del Odometer')
    fig = px.histogram(car_data, x='odometer', title='Distribución de Odometer')
    st.plotly_chart(fig)

if st.button('Mostrar Gráfico de Dispersión'):
    st.write('Gráfico de Dispersión: Precio vs Odometer')
    fig = px.scatter(car_data, x='odometer', y='price', title='Relación entre Precio y Odometer')
    st.plotly_chart(fig)

if st.checkbox('Mostrar Histograma del Odometer'):
    st.write('Histograma: Distribución del Odometer')
    fig = px.histogram(car_data, x='odometer', title='Distribución de Odometer')
    st.plotly_chart(fig)

if st.checkbox('Mostrar Gráfico de Dispersión'):
    st.write('Gráfico de Dispersión: Precio vs Odometer')
    fig = px.scatter(car_data, x='odometer', y='price', title='Relación entre Precio y Odometer')
    st.plotly_chart(fig)