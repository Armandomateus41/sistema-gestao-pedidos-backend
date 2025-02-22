import psycopg2

try:
    conn = psycopg2.connect(
        dbname="pedidos_db",
        user="postgres",
        password="123456",
        host="localhost",
        port="5432"
    )
    print("Conexão ao PostgreSQL bem-sucedida!")
    conn.close()
except Exception as e:
    print(f"Erro ao conectar: {e}")
