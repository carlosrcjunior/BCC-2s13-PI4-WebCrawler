#!/python27/python
#-*- coding: ISO-8859-1 -*-
import cgi
print "Content-type: text/html; ISO-8859-1"  
print
html1 = '''
<html>
<head>
        <title>Web Crawler</title>
</head>
<h1 align = "center"><img src = "http://www.masterstech-home.com/Links/Search_Engine_Links/WebCrawler/SurferSpidey.gif"
vspace = "20px"
hspace = "20px"
align = "center"
/></h1>
<body bgcolor="#d0d0d0" >
<p>
<h1 align="center"> Web Crawler</h1>
Site pesquisado: <strong>%s</strong></p>
<form action="formulario.py" method="post">
<p><h1 align="left"><input type="submit"     value="Voltar"/></h1>
</form>
<br><br>
</body>
</html>
'''
html2 = '''
<html>
<TABLE BORDER=3>
<TR>
<TD ALIGN=LEFT WIDTH=500><strong>Link:</strong> %s </TD>
<TD ALIGN=MIDDLE WIDTH=100><strong>ping:</strong> %d <strong>ms</strong></TD>
<TD ALIGN=MIDDLE WIDTH=250><strong>tempo de carregamento:</strong> %.3f <strong>sec</strong></TD>
<TD ALIGN=MIDDLE WIDTH=100><strong>código:</strong> %d</TD>
<TD ALIGN=LEFT WIDTH=300><strong>descrição do código:</strong> %s</TD>
</TABLE>
</p>
</html>
'''
html3 = '''
<html>
<TABLE BORDER=3>
<TR>
<TD ALIGN=LEFT WIDTH=500><strong>Link:</strong> %s </TD>
<TD ALIGN=MIDDLE WIDTH=100><strong>código:</strong> %d </TD>
<TD ALIGN=LEFT WIDTH=300><strong>descrição do código:</strong> %s</TD>
</TABLE>
</html>
'''
formulario = cgi.FieldStorage()
site = formulario.getvalue("nome")
print html1 %(site)

import urllib
import urllib2
import urlparse
import Crawler

siteurl = site
link = siteurl.strip()
final = link
fail = False
#Retorna a lista de URLs geradas
listaURL = Crawler.main(siteurl)
#Retorna o ping da URL 'principal'
latencia = Crawler.latencia(final)
if latencia == None:
    fail = True
else:
    fail = False
#Retorna o tempo de carregamento
loadTime = Crawler.loadTime(final)
#Retorna os codigos das URLs
StatusCode = Crawler.StatusCode(listaURL)
#Retorna a Descrição dos codigos
StatusCodeMsg = Crawler.StatusCodeMSG(StatusCode)

if fail == False:
    print html2 % (listaURL[0],latencia,loadTime,StatusCode[0],StatusCodeMsg[0])
elif fail == True:
    print html2 % (listaURL[0],"erro",loadTime,StatusCode[0],StatusCodeMsg[0])
aux = 0
auxURL = listaURL[1:]
auxSC = StatusCode
auxSCM = StatusCodeMsg
for list in auxURL:
    print html3 % (list,auxSC[aux],auxSCM[aux])
    aux = aux + 1
    

