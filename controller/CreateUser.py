import mysql.connector
import datetime
from utils.TestConnection import coxenao, conexao_encerrada, conexao_estabelecida

#abir conexao com o banco de dados 
connection = coxenao()

#vai no banco e conecat com o banco 
cursor = connection.cursor(dictionary=True)

sql ="INSERT INTO users(name, email,created) VALUES(%s, %s, %s)"  #sql de insercao no banco

conexao_estabelecida(connection)

#paldoy que vai passar pro banco com a query de criacao
data=(
    ' Usuario',
    'primeiro@test.com',
    datetime.datetime.today()
)


cursor.execute(sql, data) #executa a o sql e a data
connection.commit() #efetiva a query no banco

userid = cursor.lastrowid


print("O usuario foi cadastrado com sucesso com ID: ", userid)


conexao_encerrada(connection,cursor)