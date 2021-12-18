import mysql.connector

def coxenao():
    connection = mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="root",
        database="teste",

    )

    if connection.is_connected():
        db_info = connection.get_server_info()
        print("Conectado ao servidor MYSQL versao" , db_info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        linha = cursor.fetchone()
        print("Conectado ao banco e dados")
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Conectado ao servidor MYSQL foi encerrada")


coxenao()
