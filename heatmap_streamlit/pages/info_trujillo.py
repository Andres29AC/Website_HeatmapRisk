import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Informacion Trujillo",page_icon=":information_source:", layout="wide")

st.title(body=":chart_with_upwards_trend: Trujillo")

data = {
    "Categoria de Delito": [
        "Del. contra el Patrimonio", 
        "Del. contra la Seguridad Publica", 
        "Del. contra la Vida, el Cuerpo y la Salud", 
        "Del. contra la Libertad", 
        "Del. contra la Administracion Publica", 
        "Del. contra los Derechos Intelectuales", 
        "Del. contra la Familia", 
        "Del. contra la Fe Publica", 
        "Del. contra la Voluntad Popular", 
        "Del. contra el Orden Financiero y Monetario", 
        "Del. contra la Tranquilidad Publica", 
        "Del. contra la Humanidad", 
        "Del. Tributarios", 
        "Del. contra el Orden Economico", 
        "Del. Ambientales", 
        "Del. contra la Confianza y la Buena Fe en los Negocios", 
        "Del. contra el Honor"
    ],
    "Numero de Delitos (Year 2023)": [
        6879, 1952, 475, 389, 122, 53, 30, 22, 6, 6, 2, 2, 2, 2, 1, 1, 1
    ]
}

df = pd.DataFrame(data)
df_sorted = df.sort_values(by='Numero de Delitos (Year 2023)', ascending=False)

st.subheader("Tabla de Delitos:")
st.dataframe(df_sorted.style.set_table_styles([{
    'selector': 'thead th',
    'props': 'position: sticky; top: 0; background-color: #ffffff;'
}]))

st.subheader(body=":bar_chart: Grafico de Barras:")
fig = px.bar(df_sorted, x="Numero de Delitos (Year 2023)", y="Categoria de Delito", orientation='h',
             title="Numero de Delitos por Categoria (Year 2023)",
             labels={'Numero de Delitos (Year 2023)': 'Numero de Delitos', 'Categoria de Delito': 'Categoria de Delito'})
st.plotly_chart(fig)

df_part1 = df_sorted.iloc[:len(df_sorted)//2]
df_part2 = df_sorted.iloc[len(df_sorted)//2:]

categorias_otros = ["Del. contra la Administracion Publica", "Del. contra los Derechos Intelectuales", "Del. contra la Familia", "Del. contra la Fe Publica"]
df_part1['Categoria Agrupada'] = df_part1['Categoria de Delito'].apply(lambda x: x if x not in categorias_otros else 'Otros')
otros_delitos = df_part1[df_part1['Categoria de Delito'].isin(categorias_otros)]
total_otros_delitos = otros_delitos['Numero de Delitos (Year 2023)'].sum()

df_part1_agrupado = df_part1.groupby('Categoria Agrupada').sum().reset_index()
df_part1_agrupado.loc[df_part1_agrupado['Categoria Agrupada'] == 'Otros', 'Numero de Delitos (Year 2023)'] = total_otros_delitos

st.subheader("Grafico de Pastel 1:")
fig_part1_agrupado = px.pie(df_part1_agrupado, values='Numero de Delitos (Year 2023)', names='Categoria Agrupada',
                             title='Distribucion de Delitos en Trujillo',
                             hole=0.5,
                             labels={'Numero de Delitos (Year 2023)': 'Numero de Delitos'})
st.plotly_chart(fig_part1_agrupado)

st.subheader("Tabla de Otros Delitos:")
otros_delitos['Porcentaje'] = otros_delitos['Numero de Delitos (Year 2023)'] / (df_part1_agrupado[df_part1_agrupado['Categoria Agrupada'] != 'Otros']['Numero de Delitos (Year 2023)'].sum()) * 100
otros_delitos['Porcentaje'] = otros_delitos['Porcentaje'].round(2)
otros_delitos = otros_delitos.rename(columns={'Numero de Delitos (Year 2023)': 'Numero de Delitos'})

st.write(otros_delitos)

st.subheader("Grafico de Pastel 2:")
fig_part2 = px.pie(df_part2, values='Numero de Delitos (Year 2023)', names='Categoria de Delito',
                   title='Distribucion de Delitos en Trujillo',
                   hole=0.5,
                   labels={'Numero de Delitos (Year 2023)': 'Numero de Delitos'})
st.plotly_chart(fig_part2)

