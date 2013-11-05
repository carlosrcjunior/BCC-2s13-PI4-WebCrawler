from bs4 import BeautifulSoup
import urllib
import urllib2
import urlparse
import Tempo_Carregamento
import Status_Code

#Site do crawler
siteurl = raw_input('Digite o site desejado(Com http://): ')
link = siteurl.strip()
final = link

####Retirar?
###Verifica se o link começa com http://www para que o crawler possa funcionar obs: tentar sem www depois com www
##if link[:4] != "www." and link[:7] != "http://":
##    final = "http://www." + link
##    print("Formal final: " + final)
##
##if link[:4] == "www." or link[:8] == "https://":
##    final = "http://" + link
##    print("Formal final: " + final)

htmltext = urllib.urlopen(final)
soup = BeautifulSoup(htmltext)
listaURL = [final]

for tag in soup.findAll('a',href=True):
    raw = tag['href']
    b1 = urlparse.urlparse(tag['href']).hostname
    if b1 == None:
        b1 = final
    b2 = urlparse.urlparse(tag['href']).path
    #Monta a url
    #newurl = "http://" + str(b1) + str(b2)
    newurl = str(b1) + str(b2)
    #cria uma lista com todas urls
    listaURL.append(newurl)
    #print (newurl)
    
#Mostra a lista de URL's
for list in listaURL:
    print(list)

#função para calcular a latencia
print("Chamando função para calcular a latencia")
latencia = Tempo_Carregamento.PingTest(final)
print(str(latencia)+" ms")

#função para calcular o tempo de load da pagina
print("Chamando função para calcular o tempo de load da pagina")
loadTime = Tempo_Carregamento.WebLoadTime(final)
print(str(loadTime)+" sec")

#Status_Code
print ("Chamando Status Code")
codeList = Status_Code.VerificaStatus(listaURL)
for list in codeList:
    print list

#Verifica que tipo de código que é
print ("Verificando o código")
codeListMsg = Status_Code.StatusCodeList(codeList)
for list in codeListMsg:
    print list


