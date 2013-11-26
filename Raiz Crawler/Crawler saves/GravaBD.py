__author__ = 'WNUNES'
import sqlite3

def GravaBD()

    conn= sqlite3.connect(crawler.db)

    cursor= conn.cursor()


onn=sqlite.connect(‘agendas2.db’)
cursor=conn.cursor()
verif=0

while 1:
     opcao=int(raw_input(‘Para incluir contato, digite 1! Para verificar tabela,  digite 2! Para sair, digite 3: ‘))

    if opcao==1:
        nome=str(raw_input(‘Digite o seu nome completo: ‘))
        telefone=str(raw_input(‘Digite o seu numero de telefone: ‘))
        ident=int(raw_input(‘Digite o identificador do contato(ate oito   numeros): ‘))
        cursor.execute(“SELECT * FROM agenda”)
        i=0
        for linha in cursor:
            if linha[2] == ident:
                i=1
                break
        if i==0:
            cursor.execute(“INSERT INTO agenda(nome, tel, identif) VALUES(‘%s’, ‘%s’, ‘%i’)” %(nome, telefone, ident))
            conn.commit()

    if opcao==2:
       cursor.execute(“SELECT * FROM agenda”)
       print str(cursor.fetchall())
       opcao=int(raw_input(‘Para excluir um item, digite 4! Para alterar contato, digite 5! Para voltar, digite 0: ‘))

    if opcao==3:
        break

    if opcao==4:
        item=int(raw_input(‘Digite identificador do contato a ser excluido: ‘))
        cursor.execute(“DELETE FROM agenda WHERE identif=’%i’” %item)
        cursor.execute(“SELECT * FROM agenda”)
        print cursor.fetchall()
        conn.commit()

    if opcao==5:
        item=int(raw_input(‘Digite o id do contato: ‘))
        nome=str(raw_input(‘Digite um novo nome para o campo: ‘))
        telefone=str(raw_input(‘Digite um novo telefone para o campo: ‘))
        cursor.execute(“UPDATE agenda SET nome=’%s’,tel=’%s’ WHERE identif=’%i’” %(nome, telefone, item))
        cursor.execute(“SELECT * FROM agenda”)
        print cursor.fetchall()
        conn.commit()
cursor.close()
conn.close()





