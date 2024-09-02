import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="Dashboard de Vehículos", layout="wide")

# Leer el archivo CSV
@st.cache
def load_data():
    data = pd.read_csv('vehicles_us.csv')
    return data

data = load_data()

# Título de la aplicación
st.title('Análisis de Datos de Vehículos')

# Crear encabezado
st.header('Análisis Exploratorio de Datos')

# Botón para construir el histograma
if st.button('Mostrar Histograma de Odometer'):
    # Crear un histograma usando Plotly Express
    fig = px.histogram(data, x="odometer", title="Histograma de Odometer")
    # Mostrar el gráfico en la aplicación Streamlit
    st.plotly_chart(fig)

# Botón para construir el gráfico de dispersión
if st.button('Mostrar Gráfico de Dispersión'):
    # Crear un gráfico de dispersión usando Plotly Express
    fig = px.scatter(data, x="odometer", y="price", title="Gráfico de Dispersión de Odometer vs Price")
    # Mostrar el gráfico en la aplicación Streamlit
    st.plotly_chart(fig)

