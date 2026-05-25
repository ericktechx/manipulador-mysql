import mysql.connector
from mysql.connector import Error

# Funções utilitárias para conexão e manipulação de banco MySQL.
# Fluxo esperado:
#   1. criar_conexao_servidor() — conecta sem banco (para criar DBs)
#   2. criar_database()         — executa CREATE DATABASE
#   3. conectar_db()            — conecta a um banco específico
#   4. executar_query()         — INSERT, UPDATE, DELETE, CREATE TABLE
#   5. ler_query()              — SELECT (retorna lista de tuplas)
#   6. fechar_conexao()         — encerra a conexão

def criar_conexao_servidor(nome_host, nome_usuario, senha_usuario):
    """Conecta ao servidor MySQL sem selecionar um banco de dados.
    Útil para criar databases antes de conectar a elas."""
    conexao = None
    try:
        conexao = mysql.connector.connect(
            host=nome_host,
            user=nome_usuario,
            passwd=senha_usuario
        )
        print("Conexão bem-sucedida com o MySQL Server!")
    except Error as err:
        print(f"Erro ao conectar: '{err}'")
    return conexao


def criar_database(conexao, query):
    # Executa um CREATE DATABASE. Não precisa de commit.
    cursor = conexao.cursor()
    try:
        cursor.execute(query)
        print("Database criada com sucesso!")
    except Error as err:
        print(f"Erro ao criar database: '{err}'")
    finally:
        cursor.close()


def conectar_db(nome_host, nome_usuario, senha_usuario, nome_db):
    # Conecta diretamente a um banco de dados existente.
    conexao = None
    try:
        conexao = mysql.connector.connect(
            host=nome_host,
            user=nome_usuario,
            passwd=senha_usuario,
            database=nome_db
        )
        print(f"Conectado ao banco '{nome_db}' com sucesso!")
    except Error as err:
        print(f"Erro ao conectar ao banco: '{err}'")
    return conexao


def executar_query(conexao, query, valores=None):
    # Executa queries de escrita: INSERT, UPDATE, DELETE, CREATE TABLE.
    # Use 'valores' como tupla para queries parametrizadas e evitar SQL injection.
    # Exemplo: executar_query(con, 'INSERT INTO t VALUES (%s)', ('dado',))
    cursor = conexao.cursor()
    try:
        cursor.execute(query, valores) if valores else cursor.execute(query)
        conexao.commit()
        print("Query executada com sucesso!")
    except Error as err:
        print(f"Erro ao executar query: '{err}'")
    finally:
        cursor.close()


def ler_query(conexao, query, valores=None):
    # Executa um SELECT e retorna todos os resultados como lista de tuplas.
    # Retorna None em caso de erro.
    cursor = conexao.cursor()
    try:
        cursor.execute(query, valores) if valores else cursor.execute(query)
        return cursor.fetchall()
    except Error as err:
        print(f"Erro ao ler dados: '{err}'")
    finally:
        cursor.close()


def fechar_conexao(conexao):
    # Encerra a conexão com o banco de forma segura.
    if conexao and conexao.is_connected():
        conexao.close()
        print("Conexão encerrada!")
