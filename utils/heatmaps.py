import numpy as np
# Trujillo
trujillo_limites = {
    "lat_min": -8.12,
    "lat_max": -8.10,
    "lon_min": -79.04,
    "lon_max": -79.02
}
latitudes_trujillo = np.random.uniform(trujillo_limites["lat_min"], trujillo_limites["lat_max"], size=100)
longitudes_trujillo = np.random.uniform(trujillo_limites["lon_min"], trujillo_limites["lon_max"], size=100)
datos_trujillo = np.column_stack((latitudes_trujillo, longitudes_trujillo)).tolist()

data_trujillo = [
    [trujillo_limites["lat_min"], trujillo_limites["lon_min"]],
    [trujillo_limites["lat_min"], trujillo_limites["lon_max"]],
    [trujillo_limites["lat_max"], trujillo_limites["lon_min"]],
    [trujillo_limites["lat_max"], trujillo_limites["lon_max"]],
] + datos_trujillo

#Simbal
simbal_limites = {
    "lat_min": -7.985,
    "lat_max": -7.970,
    "lon_min": -78.825,
    "lon_max": -78.795
}
latitudes_simbal = np.random.uniform(simbal_limites["lat_min"], simbal_limites["lat_max"], size=100)
longitudes_simbal = np.random.uniform(simbal_limites["lon_min"], simbal_limites["lon_max"], size=100)
datos_simbal = np.column_stack((latitudes_simbal, longitudes_simbal)).tolist()
data_simbal = [
    [simbal_limites["lat_min"], simbal_limites["lon_min"]],
    [simbal_limites["lat_min"], simbal_limites["lon_max"]],
    [simbal_limites["lat_max"], simbal_limites["lon_min"]],
    [simbal_limites["lat_max"], simbal_limites["lon_max"]],
] + datos_simbal
#Poroto
poroto_limites = {
    "lat_min": -8.02,
    "lat_max": -8.005,
    "lon_min": -78.78,
    "lon_max": -78.755
}

latitudes_poroto = np.random.uniform(poroto_limites["lat_min"], poroto_limites["lat_max"], size=100)
longitudes_poroto = np.random.uniform(poroto_limites["lon_min"], poroto_limites["lon_max"], size=100)
datos_poroto = np.column_stack((latitudes_poroto, longitudes_poroto)).tolist()

data_poroto = [
    [poroto_limites["lat_min"], poroto_limites["lon_min"]],
    [poroto_limites["lat_min"], poroto_limites["lon_max"]],
    [poroto_limites["lat_max"], poroto_limites["lon_min"]],
    [poroto_limites["lat_max"], poroto_limites["lon_max"]],
] + datos_poroto
#Salaverry
salaverry_limites = {
    "lat_min": -8.245,
    "lat_max": -8.205,
    "lon_min": -78.995,
    "lon_max": -78.955
}

latitudes_salaverry = np.random.uniform(salaverry_limites["lat_min"], salaverry_limites["lat_max"], size=100)
longitudes_salaverry = np.random.uniform(salaverry_limites["lon_min"], salaverry_limites["lon_max"], size=100)
datos_salaverry = np.column_stack((latitudes_salaverry, longitudes_salaverry)).tolist()

data_salaverry = [
    [salaverry_limites["lat_min"], salaverry_limites["lon_min"]],
    [salaverry_limites["lat_min"], salaverry_limites["lon_max"]],
    [salaverry_limites["lat_max"], salaverry_limites["lon_min"]],
    [salaverry_limites["lat_max"], salaverry_limites["lon_max"]],
] + datos_salaverry
# Moche
moche_limites = {
    "lat_min": -8.18,
    "lat_max": -8.16,
    "lon_min": -79.02,
    "lon_max": -79.00
}

latitudes_moche = np.random.uniform(moche_limites["lat_min"], moche_limites["lat_max"], size=100)
longitudes_moche = np.random.uniform(moche_limites["lon_min"], moche_limites["lon_max"], size=100)
datos_moche = np.column_stack((latitudes_moche, longitudes_moche)).tolist()

data_moche = [
    [moche_limites["lat_min"], moche_limites["lon_min"]],
    [moche_limites["lat_min"], moche_limites["lon_max"]],
    [moche_limites["lat_max"], moche_limites["lon_min"]],
    [moche_limites["lat_max"], moche_limites["lon_max"]],
] + datos_moche
# Laredo
laredo_limites = {
    "lat_min": -8.095,
    "lat_max": -8.080,
    "lon_min": -78.970,
    "lon_max": -78.950
}

latitudes_laredo = np.random.uniform(laredo_limites["lat_min"], laredo_limites["lat_max"], size=100)
longitudes_laredo = np.random.uniform(laredo_limites["lon_min"], laredo_limites["lon_max"], size=100)
datos_laredo = np.column_stack((latitudes_laredo, longitudes_laredo)).tolist()

data_laredo = [
    [laredo_limites["lat_min"], laredo_limites["lon_min"]],
    [laredo_limites["lat_min"], laredo_limites["lon_max"]],
    [laredo_limites["lat_max"], laredo_limites["lon_min"]],
    [laredo_limites["lat_max"], laredo_limites["lon_max"]],
] + datos_laredo
# Porvenir
porvenir_limites = {
    "lat_min": -8.08,
    "lat_max": -8.07,
    "lon_min": -79.00,
    "lon_max": -78.98
}

latitudes_porvenir = np.random.uniform(porvenir_limites["lat_min"], porvenir_limites["lat_max"], size=100)
longitudes_porvenir = np.random.uniform(porvenir_limites["lon_min"], porvenir_limites["lon_max"], size=100)
datos_porvenir = np.column_stack((latitudes_porvenir, longitudes_porvenir)).tolist()

data_porvenir = [
    [porvenir_limites["lat_min"], porvenir_limites["lon_min"]],
    [porvenir_limites["lat_min"], porvenir_limites["lon_max"]],
    [porvenir_limites["lat_max"], porvenir_limites["lon_min"]],
    [porvenir_limites["lat_max"], porvenir_limites["lon_max"]],
] + datos_porvenir
# Esperanza
esperanza_limites = {
    "lat_min": -8.09,
    "lat_max": -8.08,
    "lon_min": -79.05,
    "lon_max": -79.03
}

latitudes_esperanza = np.random.uniform(esperanza_limites["lat_min"], esperanza_limites["lat_max"], size=100)
longitudes_esperanza = np.random.uniform(esperanza_limites["lon_min"], esperanza_limites["lon_max"], size=100)
datos_esperanza = np.column_stack((latitudes_esperanza, longitudes_esperanza)).tolist()

data_esperanza = [
    [esperanza_limites["lat_min"], esperanza_limites["lon_min"]],
    [esperanza_limites["lat_min"], esperanza_limites["lon_max"]],
    [esperanza_limites["lat_max"], esperanza_limites["lon_min"]],
    [esperanza_limites["lat_max"], esperanza_limites["lon_max"]],
] + datos_esperanza
# Florencia
florencia_limites = {
    "lat_min": -8.09,
    "lat_max": -8.07,
    "lon_min": -79.03,
    "lon_max": -79.01
}

latitudes_florencia = np.random.uniform(florencia_limites["lat_min"], florencia_limites["lat_max"], size=100)
longitudes_florencia = np.random.uniform(florencia_limites["lon_min"], florencia_limites["lon_max"], size=100)
datos_florencia = np.column_stack((latitudes_florencia, longitudes_florencia)).tolist()

data_florencia = [
    [florencia_limites["lat_min"], florencia_limites["lon_min"]],
    [florencia_limites["lat_min"], florencia_limites["lon_max"]],
    [florencia_limites["lat_max"], florencia_limites["lon_min"]],
    [florencia_limites["lat_max"], florencia_limites["lon_max"]],
] + datos_florencia
# Victor Larco
larco_limites = {
    "lat_min": -8.14,
    "lat_max": -8.12,
    "lon_min": -79.05,
    "lon_max": -79.03
}

latitudes_larco = np.random.uniform(larco_limites["lat_min"], larco_limites["lat_max"], size=100)
longitudes_larco = np.random.uniform(larco_limites["lon_min"], larco_limites["lon_max"], size=100)
datos_larco = np.column_stack((latitudes_larco, longitudes_larco)).tolist()

data_larco = [
    [larco_limites["lat_min"], larco_limites["lon_min"]],
    [larco_limites["lat_min"], larco_limites["lon_max"]],
    [larco_limites["lat_max"], larco_limites["lon_min"]],
    [larco_limites["lat_max"], larco_limites["lon_max"]],
] + datos_larco
# El Milagro
milagro_limites = {
    "lat_min": -8.05,
    "lat_max": -8.02,
    "lon_min": -79.08,
    "lon_max": -79.05
}

latitudes_milagro = np.random.uniform(milagro_limites["lat_min"], milagro_limites["lat_max"], size=100)
longitudes_milagro = np.random.uniform(milagro_limites["lon_min"], milagro_limites["lon_max"], size=100)
datos_milagro = np.column_stack((latitudes_milagro, longitudes_milagro)).tolist()

data_milagro = [
    [milagro_limites["lat_min"], milagro_limites["lon_min"]],
    [milagro_limites["lat_min"], milagro_limites["lon_max"]],
    [milagro_limites["lat_max"], milagro_limites["lon_min"]],
    [milagro_limites["lat_max"], milagro_limites["lon_max"]],
] + datos_milagro
# Huanchaco
huanchaco_limites = {
    "lat_min": -8.10,
    "lat_max": -8.06,
    "lon_min": -79.13,
    "lon_max": -79.09
}

latitudes_huanchaco = np.random.uniform(huanchaco_limites["lat_min"], huanchaco_limites["lat_max"], size=100)
longitudes_huanchaco = np.random.uniform(huanchaco_limites["lon_min"], huanchaco_limites["lon_max"], size=100)
datos_huanchaco = np.column_stack((latitudes_huanchaco, longitudes_huanchaco)).tolist()

data_huanchaco = [
    [huanchaco_limites["lat_min"], huanchaco_limites["lon_min"]],
    [huanchaco_limites["lat_min"], huanchaco_limites["lon_max"]],
    [huanchaco_limites["lat_max"], huanchaco_limites["lon_min"]],
    [huanchaco_limites["lat_max"], huanchaco_limites["lon_max"]],
] + datos_huanchaco
