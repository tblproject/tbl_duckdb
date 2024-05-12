import duckdb
import pandas

if __name__=="__main__":
    file_path = '../data/database.db'
    conn = duckdb.connect(file_path)
    
    # Get table info
    conn.sql("SHOW ALL TABLES").show()
    
    # Get local cities
    conn.sql("SELECT DISTINCT(localidad) FROM bronze.local").show()
    df = conn.sql("SELECT DISTINCT(localidad) FROM bronze.local").df()
    print(df)
    
    # Get 
    conn.sql("SELECT DISTINCT(YEAR(Periodo)) FROM bronze.nacional").show()
    conn.sql("SELECT SUM(Porcentaje) FROM bronze.nacional").show()