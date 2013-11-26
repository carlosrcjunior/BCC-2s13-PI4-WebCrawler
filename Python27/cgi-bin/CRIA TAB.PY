import sqlite3 as lite

con = lite.connect('web.db')
cursor = con.cursor()
##cursor.execute("CREATE TABLE PESQUISA(SITE TEXT,CODIGO INT,DESC TEXT)")
##con.commit()
cursor.execute("SELECT * FROM PESQUISA")
print cursor.fetchall()
cursor.close()
con.close()
