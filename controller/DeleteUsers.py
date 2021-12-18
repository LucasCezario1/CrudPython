import mysql.connector
import datetime

# abir conexao com o banco de dados
connection = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="root",
    database="teste",
)

cursor = connection.cursor()

sql = "DELETE FROM users WHERE id = %s"
data = (4,)

cursor.execute(sql, data)
connection.commit()

recordsaffected = cursor.rowcount

cursor.close()
connection.close()

print(recordsaffected," regsitro excluido com sucessso")