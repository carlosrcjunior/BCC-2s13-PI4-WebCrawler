import urllib
from bs4 import BeautifulSoup
import urlparse
import Tempo_Carregamento

#Site do crawler
siteurl = raw_input('Digite o site desejado: ')
link = siteurl.strip()
final = ""

#Verifica se o link começa com http://www para que o crawler possa funcionar
if link[:4] != "www." and link[:7] != "http://":
    final = "http://www." + link
    print("Formal final: " + final)

if link[:4] == "www.":
    final = "http://" + link
    print("Formal final: " + final)
if link[:8] == "https://":
    final = "http://" + link[8:]
    print("Formal final: " + final)
#----------------------------------------------------------------------------
htmltext = urllib.urlopen(final)
soup = BeautifulSoup(htmltext)
lista = [final]

for tag in soup.findAll('a',href=True):
    raw = tag['href']
    b1 = urlparse.urlparse(tag['href']).hostname
    if b1 == None:
        b1 = final
    b2 = urlparse.urlparse(tag['href']).path
    #Monta a url
    newurl = "http://" + str(b1) + str(b2)
    #cria uma lista com todas urls
    lista.append(newurl)
    #print (newurl)
#----------------------------------------------------------------------------   
#Lista de URL's
for list in lista:
    print(list)

#função para calcular a latencia
print("Chamando função para calcular a latencia")
latencia = Tempo_Carregamento.PingTest(final)
if (latencia == False):
    print("Site não respondeu")
elif (latencia != False):
    print (str(latencia)+"ms")
#----------------------------------------------------------------------------
#função para calcular o tempo de load da pagina
loadTime = Tempo_Carregamento.WebLoadTime(final)
print("Chamando função para calcular o tempo de load da pagina")
print(str(loadTime)+" sec")
#----------------------------------------------------------------------------


