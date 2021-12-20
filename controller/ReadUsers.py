from utils.TestConnection import coxenao, conexao_encerrada, conexao_estabelecida

# abir conexao com o banco de dados
connection = coxenao()

cursor = connection.cursor()

sql = "SELECT * FROM users"


# estabelece conexao com o banco de dados
conexao_estabelecida(connection)

cursor.execute(sql) #executa a o sql e a data
results = cursor.fetchall() #pega todos os resultados que estao no banco


#Pega todos os resultaos que estao no banco
for results in results:
    print(results)


# encerra conexao com o banco de dados
conexao_encerrada(connection, cursor)