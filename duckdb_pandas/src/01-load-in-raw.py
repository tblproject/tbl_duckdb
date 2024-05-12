import functions.work_with_duckdb as wwd
import pandas as pd

if __name__=="__main__":
    # File path to duckdb database file
    file_path = '../data/database.db'
    try:
        # Create ducdk connection
        conn  = wwd.create_duckdb_connection(file_path=file_path)
        # load CSV file in dataframe
        csv_file = pd.read_csv('../datos_base/48191.csv', delimiter=";")
        csv_file.columns = ['areas_movilidad','tipo_dato','periodo', 'porcentaje']
        csv_file['porcentaje'] = csv_file['porcentaje'].str.strip()
        csv_file['porcentaje'] = csv_file['porcentaje'].str.replace(',','.')
        csv_file['porcentaje'] = csv_file['porcentaje'].str.replace('..','0.00')
        csv_file['periodo'] = pd.to_datetime(csv_file['periodo'], format="%d/%m/%Y")
        csv_file['porcentaje'] = csv_file['porcentaje'].astype(float)
        csv_file = csv_file.drop_duplicates()
        # Load in duckdb
        wwd.load_csv_file_in_duckdb(dataframe=csv_file, table_name='raw.raw_data', conn=conn)
    
    except Exception as e:
        print(e)
    