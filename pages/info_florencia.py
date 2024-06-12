import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Informacion Florencia de Mora",page_icon=":information_source:", layout="wide")

st.title(body=":chart_with_upwards_trend: Florencia de Mora")

data = {
    "Categoria de Delito": [
        "Delitos contra el Patrimonio", 
        "Delitos contra la Seguridad Publica", 
        "Delitos contra el Vida, el Cuerpo y la Salud", 
        "Delitos contra la Libertad", 
        "Delitos contra la Administracion Publica",
        "Delitos contra la Familia",
        "Delitos contra la Fe Publica",
        "Delitos contra la Voluntad Popular",
        "Delitos contra el Orden Financiero y Monetario"
    ],
    "Numero de Delitos (Year 2023)": [315, 160, 41, 22, 16, 7, 5, 2, 1]
}

df = pd.DataFrame(data)

total_delitos = df["Numero de Delitos (Year 2023)"].sum()

st.subheader("Tabla de Delitos:")
st.dataframe(df)

st.subheader(body=":bar_chart: Grafico de Barras:")
fig = px.bar(df, x="Numero de Delitos (Year 2023)", y="Categoria de Delito", orientation='h',
             title="Numero de Delitos por Categoria (Year 2023)",
             labels={'Numero de Delitos (Year 2023)': 'Numero de Delitos', 'Categoria de Delito': 'Categoria de Delito'})
st.plotly_chart(fig)

otros_delitos = df[df['Categoria de Delito'].isin([
    "Delitos contra la Familia",
    "Delitos contra la Fe Publica",
    "Delitos contra la Voluntad Popular",
    "Delitos contra el Orden Financiero y Monetario"
])].copy()

otros_delitos_suma = otros_delitos["Numero de Delitos (Year 2023)"].sum()
otros_delitos['Porcentaje'] = (otros_delitos["Numero de Delitos (Year 2023)"] / total_delitos) * 100

df_pie = df.copy()
df_pie.loc[df_pie['Categoria de Delito'].isin(otros_delitos['Categoria de Delito']), 'Categoria de Delito'] = "Otros"

st.subheader("Grafico de Pastel:")
fig_pie = px.pie(df_pie, values='Numero de Delitos (Year 2023)', names='Categoria de Delito',
                   title='Distribucion de Delitos en Florencia de Mora (Year 2023)',
                   hole=0.5,
                   labels={'Categoria de Delito': 'Categoria de Delito', 'Numero de Delitos (Year 2023)': 'Numero de Delitos'})
st.plotly_chart(fig_pie)

st.subheader("Tabla de Otros:")
st.dataframe(otros_delitos[['Categoria de Delito', 'Numero de Delitos (Year 2023)', 'Porcentaje']])
