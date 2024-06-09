# Objetivo
El objetivo del código de este directorio es el de ver las capacidades de DuckDB para poder realizar consultas e importación de información desde archivos almacenados en un Blob Storage de Azure.


# Set de datos
Como ejemplo, se ha recurrido a descargar archivos del año 2023 del set de datos de información acerca de los taxis amarillos de New York. Estos archivos se pueden descargar desde esta URL:
https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

El diccionario de datos de estos archivos lo podéis descargar de esta web:
https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf


# Cómo prepara el entorno
Para poder probar este código, se debe:
1. Crear uin Blob Storage en Azure y un contenedor dentro del Blob Storage al que subir los archivos parquet del set de datos.
2. Crear un entorno sobre el que trabajaremos e instalaremos todas las librerías y dependencias:

```bash
python3 -m venv env
source env/bin/activate
```

3. Instalar las librerías incluidas en el archivo **requirements.txt**
```bash
pip3 install -r requirements.txt 
```