from utils.TestConnection import coxenao, conexao_encerrada, conexao_estabelecida

# abir conexao com o banco de dados
connection = coxenao()

cursor = connection.cursor()

sql = "UPDATE users SET name = %s, email = %s WHERE id = %s"


# estabelece conexao com o banco de dados
conexao_estabelecida(connection)

data = (
  'Primeiro Usuário Editado',
  'primeirousuarioeditado@teste.com.br',
  1
)

cursor.execute(sql, data)
connection.commit()

recordsaffected = cursor.rowcount


print(recordsaffected, " registros alterados")


# encerra conexao com o banco de dados
conexao_encerrada(connection, cursor)