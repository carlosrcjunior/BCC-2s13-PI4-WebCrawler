#!C:\\Python27\\python.exe
#-*- coding: ISO-8859-1 -*-
print "Content-type: text/html; ISO-8859-1"
print 

print '''
<html>
<head>
        <title>Web Crawler</title>
</head>
<body background="http://www.wingsdove.com/free-backgrounds/background-offwhite-01.jpg" text="#dc7639">
        <h1 align="center"> Web Crawler</h1>
        <br>
        <form action="processar.py" method="post">
        <p> <strong>Web Site:</strong><input type="text" name="nome" id="nome" value=""/></p>
        <br> <input type="submit"     value="Ok"/>
        </form>
</body>
</html> '''
