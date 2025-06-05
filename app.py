import pandas as pd
import streamlit as st
import plotly.express as px

import streamlit as st
import plotly.express as px
import pandas as pd

# Configurar la página
st.set_page_config(page_title="Visualización de Datos", page_icon="📊", layout="wide")

# Título de la aplicación
st.title("📊 Análisis de Datos con Plotly y Streamlit")

# Cargar dataset (puedes reemplazarlo con tu propio conjunto de datos)
df = pd.read_csv('vehicles_us.csv') 

# Sidebar para la selección
st.sidebar.header("Opciones de Gráficos")
chart_type = st.sidebar.selectbox("Selecciona el tipo de gráfico", ["Barras", "Scatter", "Líneas"])

# Crear una tabla de conteo de autos vendidos por modelo y año
model_year_counts = df.groupby(['model_year', 'model']).size().reset_index(name='count')

#configuracion para hacer zoom con scroll
config = {'scrollZoom': True}

# Crear gráfico con Plotly
if chart_type == "Barras":
    fig = px.bar(model_year_counts, x='model_year', y='count', color='model',
             title='Cantidad de carros vendidos por modelo y año')
elif chart_type == "Scatter":
    fig = px.scatter(df, x="odometer", y="price", title="Gráfico de Dispersion")
else:
    fig = px.line(model_year_counts, x='model_year', y='count', title='Tendencia de ventas de autos por año')
    fig.show(config=config)

# Mostrar gráfico en Streamlit
st.plotly_chart(fig, use_container_width=True)

# Agregar detalles
st.markdown(
    """
    ### 📝 Notas
    - Usa el sidebar para cambiar entre diferentes tipos de gráficos.
    - El gráfico de barras muestra la cantidad de autos vendidos por modelo y año.
    - El gráfico de dispersión muestra la relación entre el odómetro y el precio de los autos.
    - El gráfico de líneas muestra la tendencia de ventas de autos por año.
    """
)


hist_button = st.button('Construir histograma') # crear un botón  
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.header('Histograma de Odometer')
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')   
    # crear un histograma

    fig = px.histogram(df, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)