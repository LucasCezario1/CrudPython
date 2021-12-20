from utils.TestConnection import coxenao, conexao_encerrada, conexao_estabelecida

# abir conexao com o banco de dados
connection = coxenao()

cursor = connection.cursor()

sql = "DELETE FROM users WHERE id = %s"
data = (8,)

# estabelece conexao com o banco de dados
conexao_estabelecida(connection)

cursor.execute(sql, data)
connection.commit()

recordsaffected = cursor.rowcount


print(recordsaffected," regsitro excluido com sucessso")

# encerra conexao com o banco de dados
conexao_encerrada(connection, cursor)