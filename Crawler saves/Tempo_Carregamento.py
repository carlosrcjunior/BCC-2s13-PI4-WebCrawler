# -*- coding: cp1252 -*-
import time
import os
import urllib2
from time import time

#Calcula a latencia média do site
def PingTest(web):
    trys = 3
    ms = []
    while trys != 0:
        if (web[:7] == "http://"):
            web = web[7:]
        elif (web[:8] == "https://"):
            web = web[8:]
        strs = os.popen("ping " + web).read()
        time=strs[strs.rfind(' ')+1:strs.rfind('ms')]
        trys = trys - 1
        #Verifica se o limite de tempo de resposta foi esgotado
        if (time.isdigit() == True):
            ms.append(int(time))
        #print (trys)
    if (len(ms)>0):
        s = sum(ms)
        d = len(ms)
        media = s/d
        return media
    elif (len(ms)== 0):
        media = False
        return media
#----------------------------------------------------------------------------
#Tests
##site = raw_input ("site: ")
##time = PingTest(site)
##print (str(time)+"ms")
#----------------------------------------------------------------------------
#Calcula o tempo de carregamento
def WebLoadTime(web):
    stream = urllib2.urlopen(web)
    start_time = time()
    output = stream.read()
    end_time = time()
    stream.close()
    #tempo de carregamento
    #print(round(end_time-start_time, 3))
    tempo = round(end_time-start_time, 3)
    return tempo
#----------------------------------------------------------------------------

#Tests
##site = raw_input ("site: ")
##pingTime = PingTest(site)
##loadTime = WebLoadTime(site)
##if (pingTime == False):
##    print("Site não respondeu")
##elif (pingTime != False):
##    print (str(pingTime)+"ms")
##print ("Tempo carregamento: "+str(loadTime))
