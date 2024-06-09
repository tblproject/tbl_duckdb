import duckdb

# Create DuckDB Connection
conn = duckdb.connect(':memory:')

# Install Azure extension
conn.sql("INSTALL azure;")
conn.sql("LOAD azure;")
# This parameter is needed in Linux Systems to accept the blob storage certificate
conn.sql("SET azure_transport_option_type = curl;")

# Create a default Azure secret
conn.sql("""
         CREATE OR REPLACE PERSISTENT SECRET (
            TYPE AZURE,
            CONNECTION_STRING '<INCLUIR_AQUI_VALOR_CONNECTION_STRING>'
            );"""
         )
# Show the created secret
conn.sql("FROM duckdb_secrets();").show()

# Create the credit card parquet file
conn.sql(""" COPY
               (SELECT * FROM read_parquet('azure://xxxxxxx.blob.core.windows.net/input/*.parquet')
                  WHERE payment_type == 1)
               TO './data/00-credit-card-payment.parquet'
               (FORMAT 'parquet');""")

# Create the cash parquet file
conn.sql(""" COPY
               (SELECT * FROM read_parquet('azure://xxxxxxx.blob.core.windows.net/input/*.parquet')
                  WHERE payment_type == 2)
               TO './data/00-cash-payment.parquet'
               (FORMAT 'parquet');""")

# Show the data in credit card parquet file
conn.sql("SELECT * FROM read_parquet('./data/00-credit-card-payment.parquet')").show()





