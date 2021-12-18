import mysql.connector
import datetime


#abir conexao com o banco de dados 
connection = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="root",
    database="teste",

)

#vai no banco e conecat com o banco 
cursor = connection.cursor(dictionary=True)

sql ="INSERT INTO users(name, email,created) VALUES(%s, %s, %s)"  #sql de insercao no banco

#paldoy que vai passar pro banco com a query de criacao
data=(
    'outro Usuario',
    'primeiro@test.com',
    datetime.datetime.today()
)


cursor.execute(sql, data) #executa a o sql e a data
connection.commit() #efetiva a query no banco

userid = cursor.lastrowid

cursor.close() #fecha o script do pyton
connection.close() #fecha conexao com o banco e dados

print("O usuario foi cadastrado com sucesso com ID: ", userid)