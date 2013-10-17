import urllib
from bs4 import BeautifulSoup
import urlparse

#Site do crawler
siteurl = raw_input('Digite o site desejado: ')
link = siteurl.strip()
final = ""
#Verifica se o link começa com http://,www para que o crawler possa funcionar
if link[:4] != "www." and link[:7] != "http://":
    final = "http://www." + link
    print("Formal final: " + final)

if link[:4] == "www.":
    final = "http://" + link
    print("Formal final: " + final)

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
    
