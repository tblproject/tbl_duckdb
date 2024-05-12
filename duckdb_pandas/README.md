# Cómo preparar el entorno de trabajo

Para preparar el entorno de trabajo para probar y seguir los pasos deinfinidos en el post del blog asociado a este código, se debe hacer lo siguiente:

1. Descargarse el set de datos de prueba dentro del directorio **datos_base**. Para ello, vamos lanzar el siguiente comando dentro del directorio:

```bash
curl -lfO https://www.ine.es/jaxiT3/files/t/csv_bdsc/48191.csv
```

2. Crear un entorno sobre el que trabajaremos e instalaremos todas las librerías y dependencias:

```bash
python3 -m venv duckdb
```

3. Instalar las librerías incluidas en el archivo **requirements.txt**
```bash
pip3 install -r requirements.txt 
```

