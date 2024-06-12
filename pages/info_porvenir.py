import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Informacion El Porvenir",page_icon=":information_source:", layout="wide")

st.title(body=":chart_with_upwards_trend: El Porvenir")

data = {
    "Categoria de Delito": [
        "Delitos contra el Patrimonio",
        "Delitos contra la Seguridad Publica",
        "Delitos contra la Vida, el Cuerpo y la Salud",
        "Delitos contra la Libertad",
        "Delitos contra la Administracion Publica",
        "Delitos contra la Familia",
        "Delitos contra la Fe Publica",
        "Delitos contra el Orden Financiero y Monetario",
        "Delitos contra la Tranquilidad Publica",
        "Delitos contra la Voluntad Popular",
        "Delitos contra la Humanidad"
    ],
    "Numero de Delitos (year 2023)": [899, 350, 218, 148, 23, 16, 11, 4, 2, 1, 1]
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

otros_delitos = df[df['Categoria de Delito'].isin([
    "Delitos contra la Familia",
    "Delitos contra la Fe Publica",
    "Delitos contra el Orden Financiero y Monetario",
    "Delitos contra la Tranquilidad Publica",
    "Delitos contra la Voluntad Popular",
    "Delitos contra la Humanidad"
])].copy()

otros_delitos['Porcentaje'] = (otros_delitos['Numero de Delitos (year 2023)'] / total_delitos) * 100

otros_delitos_suma = otros_delitos["Numero de Delitos (year 2023)"].sum()

df = pd.concat([df, pd.DataFrame({"Categoria de Delito": ["Otros"], "Numero de Delitos (year 2023)": [otros_delitos_suma]})], ignore_index=True)

df_pie = df[~df['Categoria de Delito'].isin([
    "Delitos contra la Familia",
    "Delitos contra la Fe Publica",
    "Delitos contra el Orden Financiero y Monetario",
    "Delitos contra la Tranquilidad Publica",
    "Delitos contra la Voluntad Popular",
    "Delitos contra la Humanidad"
])]

st.subheader("Grafico de Pastel:")
fig_pie = px.pie(df_pie, values='Numero de Delitos (year 2023)', names='Categoria de Delito',
                 title='Distribucion de Delitos en El Porvenir (year 2023)',
                 hole=0.5,
                 labels={'Categoria de Delito': 'Categoria de Delito', 'Numero de Delitos (year 2023)': 'Numero de Delitos'})
st.plotly_chart(fig_pie)
st.subheader("Tabla de Otros Delitos:")
st.dataframe(otros_delitos[['Categoria de Delito', 'Numero de Delitos (year 2023)', 'Porcentaje']])
