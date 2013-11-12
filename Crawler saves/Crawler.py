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

if (final.count('/')>2):
    if (final[:7] == 'http://'):
        aux = final[7:]
        pos = aux.find('/') + 8
        main =final[:pos]

    elif (final[:8] == 'https://'):
        aux = final[8:]
        pos = aux.find('/') + 9
        main =final[:pos]
elif (final.count('/')==2):
    main = final

htmltext = urllib.urlopen(final)
soup = BeautifulSoup(htmltext)
listaURL = [final]

for tag in soup.findAll('a',href=True):
    raw = tag['href']
    b1 = urlparse.urlparse(tag['href']).hostname
    if b1 == None:        
        b1 = main
    b2 = urlparse.urlparse(tag['href']).path
    newurl = str(b1) + str(b2)
    #cria uma lista com todas urls
    listaURL.append(newurl)
    
#Mostra a lista de URL's
for list in listaURL:
    print(list)

#função para calcular a latencia
try:
    print("Chamando função para calcular a latencia")
    latencia = Tempo_Carregamento.PingTest(final)
    print(str(latencia)+" ms")
except ValueError:
    try:
        a = main[:len(main)-1]
        latencia = Tempo_Carregamento.PingTest(a)
        print(str(latencia)+" ms")
    except ValueError:
        print "Não foi possivel calcular o tempo de latencia"
        latencia = None

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


