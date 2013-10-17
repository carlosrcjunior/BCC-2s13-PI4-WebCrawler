import urllib
from bs4 import BeautifulSoup
import urlparse

#Site do crawler
siteurl = raw_input('Digite o site desejado: ')
print(siteurl)
link = siteurl.strip()
final = ""
#Verifica se o link começa com http:// para que o crawler possa funcionar
if link[:4] == "www.":
    final = "http://" + link

htmltext = urllib.urlopen(final)
soup = BeautifulSoup(htmltext)

for tag in soup.findAll('a',href=True):
    raw = tag['href']
    b1 = urlparse.urlparse(tag['href']).hostname
    b2 = urlparse.urlparse(tag['href']).path
    #Monta a url
    newurl = "http://"+str(b1)+str(b2)              
    print (newurl)
