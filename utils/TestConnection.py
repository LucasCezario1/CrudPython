import mysql.connector

def coxenao():
    connection = mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="root",
        database="teste",
    )
    return connection

def conexao_estabelecida(connection):
    if connection.is_connected():
        db_info = connection.get_server_info()
        print("Conectado ao servidor MYSQL versao" , db_info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        linha = cursor.fetchone()
        print("Conectado ao banco e dados")

def conexao_encerrada(connection, cursor):
    if connection.is_connected():
        print("Conexao ao servidor MYSQL foi encerrada")
        cursor.close()
        connection.close()




