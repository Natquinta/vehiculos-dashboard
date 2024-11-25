import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header('Análisis de Vehículos')

st.write('Visualización de la tabla de datos original')

st.dataframe(car_data)

st.write('Numero de datos ausentes por columna')
null_counts = car_data.isna().sum()
st.write(null_counts)

st.write('Busqueda de duplicados')
duplicates = car_data.duplicated().sum()
duplicate_rows= car_data[car_data.duplicated()]
st.write(f'Número de filas duplicadas: {duplicates}')

if duplicates > 0:
    st.write("Filas duplicadas")
    st.dataframe(duplicate_rows)
else:
    st.write("No se encontraron filas duplicadas.")


if st.button('Mostrar Gráfico de Dispersión'):
    st.write('Gráfico de Dispersión: Precio vs Odometer')
    fig = px.scatter(car_data, x='odometer', y='price', title='Relación entre Precio y Odometer')
    st.plotly_chart(fig)

if st.checkbox('Mostrar Histograma del Odometer'):
    st.write('Histograma: Distribución del Odometer')
    fig = px.histogram(car_data, x='odometer', title='Distribución de Odometer')
    st.plotly_chart(fig)