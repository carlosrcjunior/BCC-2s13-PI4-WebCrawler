#-*- coding: ISO-8859-1 -*-
import urllib
import urllib2
import urlparse
import Crawler

siteurl = raw_input('Digite o site desejado(Com http://): ')
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
#Retorna a Descri��o dos codigos
StatusCodeMsg = Crawler.StatusCodeMSG(StatusCode)


