import functions.work_with_duckdb as wwd
import configs.sql_sentences as sqls

if __name__=="__main__":
    try:
        # File path to duckdb database file
        file_path = '../data/database.db'
        # Create ducdk connection
        conn  = wwd.create_duckdb_connection(file_path=file_path)
        # Insert in bronze tables
        wwd.insert_duckbd_table(sentence=sqls.insert_data_in_nacional, conn=conn)
        wwd.insert_duckbd_table(sentence=sqls.insert_data_in_local, conn=conn)
    except Exception as e:
        print(e)