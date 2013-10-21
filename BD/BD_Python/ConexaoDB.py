# -*- coding: cp1252 -*-
# Teste DB
import sqlite3

c = sqlite3.Connection('teste.db')
cursor = c.cursor()


cursor.execute('INSERT INTO FUNCIONARIO (Id,"Nome") values (22,"Reginaldo ROSSI")')
cursor.execute('SELECT * FROM FUNCIONARIO')
c.commit()# Conclui operação no BD


dados = cursor.fetchall()

for exibir in dados:

    print exibir
