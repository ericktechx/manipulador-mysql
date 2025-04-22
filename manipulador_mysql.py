import mysql.connector
from mysql.connector import Error

# Funções com os principais passos para criação e manipulação de um Banco de Dados.
def criar_conexão_servidor(nome_host, nome_usuário, senha_usuário):
    conexão = None
    try:
        conexão = mysql.connector.connect(
            host = nome_host,
            user = nome_usuário,
            passwd = senha_usuário
        )
        print("Conexão bem-sucedida com o MySQL-Server!")
    except Error as err:
        print(f"Erro: '{err}'")
    return conexão


def criar_database(conexão, query):
    cursor = conexão.cursor()
    try:
        cursor.execute(query)
        print("Database criada com sucesso!")
    except Error as err:
        print(f"Erro: '{err}'")


def conectar_db(nome_host, nome_usuário, senha_usuário, nome_db):
    conexão = None
    try:
        conexão = mysql.connector.connect(
            host = nome_host,
            user = nome_usuário,
            passwd = senha_usuário,
            database = nome_db
        )
        print("MySQL Database conexão bem-sucedida!")
    except Error as err:
        print(f"Erro: '{err}'")
    return conexão


def executar_query(conexão, query):
    cursor = conexão.cursor()
    try:
        cursor.execute(query)
        conexão.commit()
        print("Query bem-sucedida!")
    except Error as err:
        print(f"Erro: '{err}'")
