import duckdb
import pandas as pd

def create_duckdb_connection(file_path:str):
    """ Function to create duckdb connection and duckdb file.

    Args:
        file_path (str): file path to duckdb file.

    Returns:
        duckdb connection: duckdb connection and duckdb file.
    """
    try:
        conn = duckdb.connect(file_path)
    except Exception as e:
        print(e)
        raise
    return conn


def create_duckdb_table(sentence:str, conn):
    """Function to create e new duckdb table.

    Args:
        create_sentence (str): SQL sentence to create the duckdb table.
        conn (duckdb connection): the ducdb connection 
    """
    try:
        conn.sql(sentence)
    except Exception as e:
        print(e)
        raise
create_duckdb_schema = create_duckdb_table
insert_duckbd_table  = create_duckdb_table

def select_duckbd_table(sentence:str, conn):
    """Function to exec SELECT query

    Args:
        sentence (str): SQL sentence.
        conn (duckdb connection): the ducdb connection 
    """
    sql_result = pd.DataFrame()
    try:
        sql_result = conn.sql(sentence).df()
    except Exception as e:
        print(e)
        raise
    return sql_result

def drop_duckdb_table(table_name:str, conn):
    """Function to drop e  duckdb table.

    Args:
        table_name (str): the table name to drop
        conn (duckdb connection): the ducdb connection 
    """
    try:
        conn.sql(f"DROP TABLE IF EXISTS {table_name} ")
    except Exception as e:
        print(e)
        raise

    
def load_csv_file_in_duckdb(dataframe, table_name:str, conn:any):
    """Function to load the csv file data in a new duckdb table.

    Args:
        create_sentence (str): SQL sentence to create the duckdb table.
        conn (duckdb connection): the ducdb connection 
    """
    try:
        df = dataframe
        # Create table and insert Data
        conn.sql(f"CREATE TABLE {table_name} AS SELECT * FROM df")
    except Exception as e:
        print(e)
        raise