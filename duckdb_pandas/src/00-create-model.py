import functions.work_with_duckdb as wwd
import configs.sql_sentences as sqls

if __name__=="__main__":
    # File path to duckdb database file
    file_path = '../data/database.db'
    try:
        # Create ducdk connection
        conn  = wwd.create_duckdb_connection(file_path=file_path)
        # Create schemas
        wwd.create_duckdb_schema(sentence=sqls.create_raw_schema, conn=conn)
        wwd.create_duckdb_schema(sentence=sqls.create_bronze_schema, conn=conn)
        # Create Bronze tables
        wwd.create_duckdb_table(sentence=sqls.create_total_nacional, conn=conn)
        wwd.create_duckdb_table(sentence=sqls.create_total_local, conn=conn)
    except Exception as e:
        print(e)
    