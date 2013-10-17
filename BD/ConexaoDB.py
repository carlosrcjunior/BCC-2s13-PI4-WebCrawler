# -*- coding: cp1252 -*-
# Teste DB
# Verificar não grava no DB
import sqlite3 as lite

c = lite.connect('teste.db')
cursor = c.cursor()

#cursor.execute('SELECT * FROM CADASTRO')

#cursor.execute("INSERT INTO FUNCIONARIO (id,Nome) values (12,'Alberto')")
#cursor.execute("CREATE TABLE CADASTRO(Id INT, Name TEXT)")
cursor.execute("INSERT INTO CADASTRO VALUES(1900 , 'JOSE')")
cursor.execute("INSERT INTO CADASTRO VALUES(1000 , 'JORGE')")
cursor.execute("INSERT INTO CADASTRO VALUES(2 , 'JUVENAL')")
cursor.commit()
cursor.execute('SELECT * FROM CADASTRO')

dados = cursor.fetchall() 

print dados

