#!/python27/python
#-*- coding: ISO-8859-1 -*-
import cgi
print "Content-type: text/html; ISO-8859-1"  
print
html1 = '''
<html>
<head>
        <title>Seus dados</title>
</head>
<body background="http://www.wingsdove.com/free-backgrounds/background-offwhite-01.jpg" >
<p>
<h1 align="center"> Web Crawler</h1>
Site pesquisado: <strong>%s</strong></p>

<br><br>
</body>
</html>
'''
html2 = '''
<html>
Link %s ping de %d ms <br>Tempo de carregamento %d <br>código %d <br>descrição do código %s<br>
</p>
</html>
'''

formulario = cgi.FieldStorage()
nome = formulario.getvalue("nome")
a = 0
print html1 %(nome)

import urllib
import urllib2
import urlparse
import Crawler

siteurl = nome
link = siteurl.strip()
final = link
#Retorna a lista de URLs geradas
listaURL = Crawler.main(siteurl)
#Retorna o ping da URL 'principal'
latencia = Crawler.latencia(final)
#Retorna o tempo de carregamento
loadTime = Crawler.loadTime(final)
#Retorna os codigos das URLs
StatusCode = Crawler.StatusCode(listaURL)
#Retorna a Descrição dos codigos
StatusCodeMsg = Crawler.StatusCodeMSG(StatusCode)


print html2 % (listaURL[0],latencia,loadTime,StatusCode[0],StatusCodeMsg[0])
    

