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
        if web[:7] == "http://":
            web = web[7:]
        elif web[:8] == "https://":
            web = web[8:]
        strs = os.popen("ping " + web).read()
        time=strs[strs.rfind(' ')+1:strs.rfind('ms')]
        trys = trys - 1
        ms.append(int(time))
        #print (trys)
    s = sum(ms)
    d = len(ms)
    media = s/d
    return media

##site = raw_input ("site: ")
##time = PingTest(site)
##print (str(time)+"ms")

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
