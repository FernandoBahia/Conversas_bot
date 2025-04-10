# Conversas_bot
Script em Python e Database MySQL para criação de histórico de conversa que sera implementado no código de um colega que esta criando um Bot para automatizar atendimentos.


- No seu SGBD de preferencia siga os passos a seguir
- Criar o database que sera usado, no caso foi criado o "db_conversasbot" no MySQL
- Criar a tabela que sera ultilizada, criei a tabela "conversas"
- Atribuir os campos necessários para o funcionaneto do database, foram adiconados os campos "ID, numero_contato, mensagem_enviada e resposta_bot"
- Apos isso se necessário popule a tabela, inseri alguns dados ficticios nos campos para demonstração

- Agora usando alguma IDE para codar
- Ultilizei o Vs Code e importei as bibliotecas "mysql.connector" para conectar ao MySql e o "time" que é para manipular o tempo
 - Apos isso inicei a configuração e setei os paramentros do ambiente 

conn = mysql.connector.connect(...): Estabelece uma conexão com o servidor MySQL usando as credenciais fornecidas.
cursor = conn.cursor(): Cria um cursor para executar comandos SQL.
cursor.execute('CREATE DATABASE IF NOT EXISTS db_conversasbot'): Cria o banco de dados db_conversasbot se ele não existir.
cursor.execute('USE db_conversasbot'): Seleciona o banco de dados db_conversasbot para uso.
cursor.execute('CREATE TABLE IF NOT EXISTS conversas (...)'): Cria a tabela conversas com os campos id, numero_contato, mensagem_enviada e resposta_bot se ela não existir.
conn.commit(): Confirma as alterações feitas no banco de dados.
conn.close(): Fecha a conexão com o banco de dados.
conn = mysql.connector.connect(...): Conecta ao banco de dados db_conversasbot.
cursor = conn.cursor(): Cria um cursor para executar comandos SQL.
cursor.execute('INSERT INTO Conversas (...) VALUES (%s, %s, %s)', (numero_contato, mensagem_enviada, resposta_bot)): Insere uma nova linha na tabela conversas com os valores fornecidos.
conn.commit(): Confirma a inserção dos dados.
conn.close(): Fecha a conexão com o banco de dados.
conn = mysql.connector.connect(...): Conecta ao banco de dados db_conversasbot.
cursor = conn.cursor(): Cria um cursor para executar comandos SQL.
cursor.execute('DELETE FROM Conversas WHERE numero_contato = %s', (numero_contato,)): Exclui todas as linhas da tabela conversas onde o numero_contato corresponde ao valor fornecido.
conn.commit(): Confirma a exclusão dos dados.
conn.close(): Fecha a conexão com o banco de dados.
criar_banco(): Cria o banco de dados e a tabela.
armazenar_conversa(...): Armazena uma conversa de exemplo.
time.sleep(10): Pausa a execução por 10 segundos para simular inatividade.
apagar_conversa(...): Apaga a conversa do banco de dados após o período de inatividade.
