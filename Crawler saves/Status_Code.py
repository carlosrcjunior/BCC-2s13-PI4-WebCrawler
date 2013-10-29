# -*- coding: cp1252 -*-
import urllib2
import urllib
import httplib

##Retorna status da pagina requisitada
def get_status_code(host, path="/"):
    try:
        conn = httplib.HTTPConnection(host)
        conn.request("HEAD", path)
        resp = conn.getresponse().status
        print resp
        return resp
    except StandardError:
        print('StandardError')
        return True
#-----------------------------------------------------------------
##lista=['www.google.com/a/b','www.uol.com.br','www.a.com.br','stackoverflow.com/nonexistant']
##errolist = []
def VerificaStatus(lista):
    errolist = []
    for list in lista:
        split = list.split('/')
        if(len(split)==1):
            volta = get_status_code(list)
        elif(len(split)!=1):
            path = split[1:]
            path2 = ''
            for list in path:
                a = list
                path2 = path2+'/'+a
            volta = get_status_code(split[0],path2)
        #Monta o errolist
        if volta == True:
            errolist.append(True)
        elif volta >= 400:
            errolist.append(True)
        elif volta < 400:
            errolist.append(False)
    return errolist
        
##print 'Saiu do For'
##print errolist
