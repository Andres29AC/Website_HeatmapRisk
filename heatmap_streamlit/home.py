import base64
import os
from utils.coordinates import wind_locations as loc
from utils.heatmaps import data_larco, data_porvenir, data_esperanza, data_florencia, data_laredo, data_poroto, data_milagro, data_huanchaco, data_salaverry, data_moche, data_simbal, data_trujillo
from folium.plugins import MousePosition, LocateControl, MiniMap, Fullscreen, AntPath, HeatMap
import folium as fo
import streamlit as st
from streamlit_folium import st_folium
import time

st.set_page_config(page_title="HeatMap Risk",
                   page_icon=":world_map:",
                   layout="wide"
                   )

st.title(body=":world_map: Mapa de Riesgo de Trujillo")

with st.expander(label=":clipboard: Objetivo:", expanded=False):
    st.write('''
       El objetivo del mapa es mostrar la distribucion delictiva mediante mapas de calor en cada distrito de Trujillo.
    ''')

st.sidebar.title(":chart: Estadisticas:")

st.sidebar.info(
    "Informacion sobre los delitos mas comunes en cada distrito de **Trujillo**."
)
st.sidebar.info(
    "Esta informacion fue extraida de [DATACRIM](https://datacrim.inei.gob.pe/panel/mapa) la plataforma del INEI."
)

if st.sidebar.button(label=":cityscape: Trujillo"):
    st.switch_page("pages/info_trujillo.py")
if st.sidebar.button(label=":cityscape: Laredo"):
    st.switch_page("pages/info_laredo.py")
if st.sidebar.button(label=":cityscape: Florencia de Mora"):
    st.switch_page("pages/info_florencia.py")
if st.sidebar.button(label=":cityscape: Moche"):
    st.switch_page("pages/info_moche.py")
if st.sidebar.button(label=":cityscape: Huanchaco"):
    st.switch_page("pages/info_huanchaco.py")
if st.sidebar.button(label=":cityscape: Porvenir"):
    st.switch_page("pages/info_porvenir.py")
if st.sidebar.button(label=":cityscape: Salaverry"):
    st.switch_page("pages/info_salaverry.py")
if st.sidebar.button(label=":cityscape: Victor Larco Herrera"):
    st.switch_page("pages/info_larco.py")
if st.sidebar.button(label=":cityscape: La Esperanza"):
    st.switch_page("pages/info_esperanza.py")
if st.sidebar.button(label=":cityscape: Simbal"):
    st.switch_page("pages/info_simbal.py")
if st.sidebar.button(label=":cityscape: Poroto"):
    st.switch_page("pages/info_poroto.py")

selectstyle = st.sidebar.selectbox("Selecciona un estilo de mapa", [
    "OpenStreetMap", "OpenStreetMap.Mapnik", "Stadia.Outdoors",
    "Esri.WorldImagery", "Stadia.OSMBright",
])
mloc = fo.Map(location=[-8.0832764, -79.2538991], popup="Mi Ubicacion", zoom_start=10, tiles=selectstyle)


def img_to_base64(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, "rb") as file:
        data = file.read()
    return base64.b64encode(data).decode()

assets_dir = "assets"
if not os.path.isdir(assets_dir):
    st.error(f"Directory not found: {assets_dir}")
else:
    files_in_assets = os.listdir(assets_dir)
    st.write(f"Files in '{assets_dir}': {files_in_assets}")

feature_groups = {
    "Trujillo": ([-8.11377086088365, -79.0294647216797],"La Ciudad de la Eterna Primavera","https://es.wikipedia.org/wiki/Trujillo_(Per%C3%BA)", "assets/trujillo.jpg", fo.Icon(color="green", icon="city", prefix="fa")),
    "Huanchaco": ([-8.081140480885056, -79.1173553466797],"El lugar de los Caballitos de Totora","https://es.wikipedia.org/wiki/Huanchaco", "assets/huanchaco.jpg", fo.Icon(color="black", icon="city", prefix="fa")),
    "Salaverry": ([-8.225577732458298, -78.97556304931642],"El Puerto historico","https://es.wikipedia.org/wiki/Distrito_de_Salaverry#:~:text=Salaverry%20es%20una%20localidad%20de,del%20departamento%20de%20La%20Libertad.", "assets/salaverry.jpg", fo.Icon(color="orange", icon="city", prefix="fa")),
    "Laredo": ([-8.086612699415404, -78.95934104919435],"La Joya Serena","https://es.wikipedia.org/wiki/Distrito_de_Laredo", "assets/laredo.jpg", fo.Icon(color="blue", icon="city", prefix="fa")),
    "Moche": ([-8.172226993083338, -79.00955200195314],"La Ciudad de las Piramides","https://es.wikipedia.org/wiki/Distrito_de_Moche", "assets/moche.jpg", fo.Icon(color="purple", icon="city", prefix="fa")),
    "Victor Larco": ([-8.132386270397017, -79.04474258422853],"El Distrito Jardin","https://es.wikipedia.org/wiki/Distrito_de_V%C3%ADctor_Larco_Herrera", "assets/larco.jpg", fo.Icon(color="gray", icon="city", prefix="fa")),
    "Florencia de Mora": ([-8.082592193271534, -79.0239715576172],"El Distrito del Comercio","https://es.wikipedia.org/wiki/Distrito_de_Florencia_de_Mora", "assets/florencia.jpg", fo.Icon(color="darkgreen", icon="city", prefix="fa")),
    "La Esperanza": ([-8.083781884673302, -79.04062271118165],"El Distrito Dormitorio","https://es.wikipedia.org/wiki/Distrito_de_La_Esperanza_(Trujillo)", "assets/esperanza.jpg", fo.Icon(color="cadetblue", icon="city", prefix="fa")),
    "El Porvenir": ([-8.074604174460923, -78.99307250976562],"El Distrito del Calzado","https://es.wikipedia.org/wiki/Distrito_de_El_Porvenir", "assets/porvenir.jpg", fo.Icon(color="darkblue", icon="city", prefix="fa")),
    "Simbal": ([-7.977793585163323, -78.81351470947267],"El Refugio de las Montañas","https://es.wikipedia.org/wiki/Distrito_de_Simbal", "assets/simbal.jpg", fo.Icon(color="darkred", icon="city", prefix="fa")),
    "Poroto": ([-8.013492029841098, -78.76647949218751],"El Oasis verde","https://es.wikipedia.org/wiki/Distrito_de_Poroto", "assets/poroto.jpg", fo.Icon(color="darkpurple", icon="city", prefix="fa"))
}

for city, (coords, description, additional, img_path, icon) in feature_groups.items():
    try:
        img_base64 = img_to_base64(img_path)
    except FileNotFoundError as e:
        st.error(f"Error: {e}")
        continue
    popup_content = f'''
    <div style="width: 200px; height: 270px; overflow: hidden;border-radius: 8px; background-color: white; margin:20px;box-shadow: 0 2 4px rgba(0, 0, 0, 0.2);">
        <img src="data:image/jpeg;base64,{img_base64}" style="width: 100%; height: auto; border-radius: 10px;box-shadow: 0 0 10px rgba(0, 0, 0, 0.7);">
        <div style="padding:16px;">
          <h4 style="text-align: center; font-weight: bold; margin-bottom: 8px; font-size:21px;">{city}</h4>
          <p style="text-align: center;color:#666;font-size:13px;line-height:1.3;">{description}</p>
          <div style="text-align: center;">
            <a href="{additional}" target="_blank" style="font-size:12px;display:inline-block;background-color:#3498db;color:#fff;text-decoration:none;border-radius:5px;padding:8px 16px;">Mas Informacion</a>
          </div>
        </div>
    </div>
    '''
    fo.Marker(location=coords, tooltip=city, icon=icon, popup=popup_content).add_to(mloc)

heatmap_data = {
    "Trujillo": data_trujillo,
    "Huanchaco": data_huanchaco,
    "Salaverry": data_salaverry,
    "Laredo": data_laredo,
    "Moche": data_moche,
    "Victor Larco": data_larco,
    "Florencia de Mora": data_florencia,
    "La Esperanza": data_esperanza,
    "El Porvenir": data_porvenir,
    "Simbal": data_simbal,
    "Poroto": data_poroto
}

for city, data in heatmap_data.items():
    fg = fo.FeatureGroup(name=city)
    HeatMap(data, radius=10).add_to(fg)
    fg.add_to(mloc)

formatter = "function(num) {return L.Util.formatNum(num, 3) + ' &deg; ';};"
MousePosition(
    position="topright",
    separator=" | ",
    empty_string="NaN",
    lng_first=True,
    num_digits=20,
    prefix="Coordinates:",
    lat_formatter=formatter,
    lng_formatter=formatter,
).add_to(mloc)

fo.LayerControl(collapsed=True).add_to(mloc)

LocateControl(auto_start=False, strings={"title": "See your current location", "popup": "Mi ubicacion"}).add_to(mloc)

Fullscreen(position="topright", title="Expand me", title_cancel="Exit me", force_separate_button=True).add_to(mloc)

MiniMap().add_to(mloc)

AntPath(locations=loc, reverse=True, dash_array=[10, 20]).add_to(mloc)
mloc.fit_bounds(mloc.get_bounds())

st_data = st_folium(mloc, width=700, height=500)
