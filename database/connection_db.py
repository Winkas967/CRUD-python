import psycopg, os
from psycopg.rows import dict_row

def get_db_connection():
    try:
        connection = psycopg.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            row_factory=dict_row
        )
            
        cursor = connection.cursor()
        
        return connection, cursor
    except Exception as e:
        raise Exception(f"Erro ao se conectar com postgress: {str(e)}")
