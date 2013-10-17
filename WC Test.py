import urllib
from bs4 import BeautifulSoup
import urlparse

htmltext = urllib.urlopen("http://nytimes.com")
soup = BeautifulSoup(htmltext)

for tag in soup.findAll('a',href=True):
    raw = tag['href']					#Mostra todos os links do site
    b1 = urlparse.urlparse(tag['href']).hostname	#Mostra somente o host dos links
    print raw						#print b1
