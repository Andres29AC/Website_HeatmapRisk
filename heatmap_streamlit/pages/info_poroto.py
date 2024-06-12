import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Informacion Poroto",page_icon=":information_source:", layout="wide")

st.title(body=":chart_with_upwards_trend: Poroto")

data = {
    "Categoria de Delito": [
        "Delitos contra el Patrimonio",
        "Delitos contra la Vida, el Cuerpo y la Salud",
        "Delitos contra la Familia",
        "Delitos contra la Libertad",
        "Delitos contra la Administracion Publica",
        "Delitos contra la Seguridad Publica"
    ],
    "Numero de Delitos (year 2023)": [26, 12, 3, 1, 1, 1]
}

df = pd.DataFrame(data)

total_delitos = df["Numero de Delitos (year 2023)"].sum()

st.subheader("Tabla de Delitos:")
st.dataframe(df)

st.subheader(body=":bar_chart: Grafico de Barras:")
fig = px.bar(df, x="Numero de Delitos (year 2023)", y="Categoria de Delito", orientation='h',
             title="Numero de Delitos por Categoria (year 2023)",
             labels={'Numero de Delitos (year 2023)': 'Numero de Delitos', 'Categoria de Delito': 'Categoria de Delito'})
st.plotly_chart(fig)

st.subheader("Grafico de Pastel:")
fig_pie = px.pie(df, values='Numero de Delitos (year 2023)', names='Categoria de Delito',
                 title='Distribucion de Delitos en Poroto (year 2023)',
                 hole=0.5,
                 labels={'Categoria de Delito': 'Categoria de Delito', 'Numero de Delitos (year 2023)': 'Numero de Delitos'})
st.plotly_chart(fig_pie)
