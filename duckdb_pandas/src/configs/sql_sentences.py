create_raw_schema = "CREATE SCHEMA IF NOT EXISTS RAW"
create_bronze_schema = "CREATE SCHEMA IF NOT EXISTS BRONZE" 
create_total_nacional = """
    CREATE TABLE IF NOT EXISTS bronze.nacional (
        Periodo TIMESTAMP_NS,
        Porcentaje FLOAT8 NOT NULL,
        PRIMARY KEY(Periodo, Porcentaje)
    )
"""

create_total_local = """
    CREATE TABLE IF NOT EXISTS bronze.local (
        Periodo TIMESTAMP_NS,
        Localidad VARCHAR NOT NULL,
        Porcentaje FLOAT8 NOT NULL,
        PRIMARY KEY(Periodo, Localidad, Porcentaje)
    )
"""

insert_data_in_nacional = """
    INSERT INTO bronze.nacional 
    SELECT periodo, porcentaje FROM raw.raw_data
    WHERE areas_movilidad LIKE 'Total Nacional'
    """
    
insert_data_in_local = """
    INSERT INTO bronze.local 
    SELECT periodo, areas_movilidad, porcentaje FROM raw.raw_data
    WHERE areas_movilidad NOT LIKE 'Total Nacional'
    """