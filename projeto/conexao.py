import mysql.connector
from mysql.connector import Error

def conectar_banco():
    """Conecta ao banco de dados sistema_escola"""
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            database='sistema_escola',
            user='root',
            password='',
            port=3306
        )
        print("✅ Conectado ao banco sistema_escola!")
        return conexao
    except Error as e:
        print(f"❌ Erro ao conectar: {e}")
        return None
