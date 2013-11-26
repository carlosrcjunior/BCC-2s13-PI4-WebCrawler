import sqlite3 as lite
def gravaBD(site,SC,SCMSG):
    con = lite.connect('web.db')

    cursor = con.cursor()
    #cursor.execute("SELECT * FROM PESQUISA")
    cursor.execute("INSERT INTO PESQUISA(SITE,CODIGO,DESC) VALUES('%s','%d','%s')"%(site,SC,SCMSG))
    con.commit()
    cursor.close()
    con.close()
    return
def mostraBD():
    
    con = lite.connect('web.db')

    cursor = con.cursor()
    cursor.execute("SELECT * FROM PESQUISA")
    print cursor.fetchall()
    cursor.close()
    con.close()
