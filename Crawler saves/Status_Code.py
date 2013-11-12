# -*- coding: cp1252 -*-
import urllib2
import urllib
import httplib


msgCodeInt = [100,101,122,200,201,202,203,204,205,206,207,300,301,302,304,
              305,306,307,400,401,402,403,404,405,406,407,408,409,410,411,
              412,413,414,415,416,417,418,422,423,424,425,426,450,499]

##Retorna status da pagina requisitada
def GetStatusCode(host, path="/"):
    try:
        conn = httplib.HTTPConnection(host)
        conn.request("HEAD", path)
        resp = conn.getresponse().status
        #print resp
        return resp
    except StandardError:
        #print('StandardError')
        return True
#-----------------------------------------------------------------

def VerificaStatus(lista):
    errolist = []
    for list in lista:
        if list[:7] == "http://":
            list = list[7:]
        split = list.split('/')
        if(len(split)==1):
            volta = GetStatusCode(list)
        elif(len(split)!=1):
            path = split[1:]
            path2 = ''
            for list in path:
                a = list
                path2 = path2+'/'+a
            volta = GetStatusCode(split[0],path2)
            errolist.append(volta)
    return errolist
#-----------------------------------------------------------------

def StatusCodeList(code):
    msg = []
    for list in code:		
	if list >= 100 and list < 200:
            msg.append("Mensagem Informativa")
	elif list >= 200 and list < 300:
            msg.append("Mensagem de Sucesso")
	elif list >= 300 and list < 400:
            msg.append("Mensagem de Redirecionamento")
	elif list >= 400 and list < 500:
            msg.append("Mensagem de Erro de Cliente")
	else:
            msg.append("Código não Encontrado")
    return msg

#-----------------------------------------------------------------
