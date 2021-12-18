import mysql.connector
#from utils.TestConnection import coxenao

# abir conexao com o banco de dados
connection = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="root",
    database="teste",
)

cursor = connection.cursor()

sql = "SELECT * FROM users"

cursor.execute(sql) #executa a o sql e a data
results = cursor.fetchall() #pega todos os resultados que estao no banco

cursor.close()
connection.close()

#Pega todos os resultaos que estao no banco
for results in results:
    print(results)
