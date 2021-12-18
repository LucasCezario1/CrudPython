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

sql = "UPDATE users SET name = %s, email = %s WHERE id = %s"
data = (
  'Primeiro Usuário Editado',
  'primeirousuarioeditado@teste.com.br',
  1
)

cursor.execute(sql, data)
connection.commit()

recordsaffected = cursor.rowcount

cursor.close()
connection.close()

print(recordsaffected, " registros alterados")