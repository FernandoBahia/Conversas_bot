import mysql.connector
import time

def criar_banco():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='sua_senha'
    )
    cursor = conn.cursor()
    cursor.execute('CREATE DATABASE IF NOT EXISTS db_conversasbot')
    cursor.execute('USE db_conversasbot')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS conversas (
            id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
            numero_contato VARCHAR(30) NOT NULL,
            mensagem_enviada TEXT NOT NULL,
            resposta_bot TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def armazenar_conversa(numero_contato, mensagem_enviada, resposta_bot):
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='sua_senha',
        database='db_conversasbot'
    )
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Conversas (numero_contato, mensagem_enviada, resposta_bot)
        VALUES (%s, %s, %s)
    ''', (numero_contato, mensagem_enviada, resposta_bot))
    conn.commit()
    conn.close()

def apagar_conversa(numero_contato):
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Cadeado01@',
        database='db_conversasbot'
    )
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM Conversas WHERE numero_contato = %s
    ''', (numero_contato,))
    conn.commit()
    conn.close()


criar_banco()
armazenar_conversa('+55 61 8456-0772', 'Olá, tudo bem?', 'Estou bem, e você?')


time.sleep(10)  
apagar_conversa('+55 61 8456-0772')
