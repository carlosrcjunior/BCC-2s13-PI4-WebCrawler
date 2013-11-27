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
<p>
<font face = "arial">
<h1 align="center"> Web Crawler</h1></p>
<h1 align = "center"><img src = "http://img.viralpatel.net/web-crawler.gif"/></h1>
<body >


<form action="formulario.py" method="post">
<p><h1 align="right"><input type="submit"     value="Voltar"/></h1>
</form>
<br><br>
</body>
</font>
</html>
'''
html2 = '''
<html>
<font face = "arial">
<TABLE BORDER=0>
<TR>
<TD ALIGN=LEFT WIDTH=300><strong>LINK:</strong> %s </TD>
<TD ALIGN=MIDDLE WIDTH=150><strong>PING:</strong> %d <strong>ms</strong></TD>
<TD ALIGN=MIDDLE WIDTH=350><strong>TEMPO DE CARREGAMENTO:</strong> %.3f <strong>sec</strong></TD>
<TD ALIGN=MIDDLE WIDTH=150><strong>CÓDIGO:</strong> %d</TD>
<TD ALIGN=LEFT WIDTH=600><strong>DESCRIÇÃO DO CÓDIGO:</strong> %s</TD>
</TABLE>
</font>
</p>
</html>
'''
html3 = '''
<html>
<font face = "arial">
<TABLE BORDER=0>
<TR>
<TD ALIGN=MIDDLE WIDTH=30><strong>%d</strong></TD>
<TD ALIGN=LEFT WIDTH=500>%s </TD>
<TD ALIGN=MIDDLE WIDTH=100>%d </TD>
<TD ALIGN=LEFT WIDTH=300>%s</TD>
</TABLE>
</font>
</html>
'''
html4 = '''
<html>
<font face = "arial">
<TABLE BORDER=0>
<TR>
<TD WIDTH=30></TD>
<TD ALIGN=LEFT WIDTH=500><strong>LINK:</strong></TD>
<TD ALIGN=MIDDLE WIDTH=100><strong>CÓDIGO:</strong></TD>
<TD ALIGN=LEFT WIDTH=300><strong>DESCRIÇÃO DO CÓDIGO:</strong></TD>
</TABLE>
</font>
</html>
'''
formulario = cgi.FieldStorage()
site = formulario.getvalue("nome")
print html1
import urllib
import urllib2
import urlparse
import BD
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
    BD.gravaBD(listaURL[0],StatusCode[0],StatusCodeMsg[0])
elif fail == True:
    print html2 % (listaURL[0],"erro",loadTime,StatusCode[0],StatusCodeMsg[0])
    BD.gravaBD(listaURL[0],StatusCode[0],StatusCodeMsg[0])

print html4
aux = 0
auxURL = listaURL[1:]
auxSC = StatusCode
auxSCM = StatusCodeMsg
for list in auxURL:
    BD.gravaBD(list,auxSC[aux],auxSCM[aux])
    print html3 % (aux+1,list,auxSC[aux],auxSCM[aux])
    aux = aux + 1
    
