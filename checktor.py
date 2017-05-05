#!/usr/bin/env python

import apache_log_parser
import urllib2

# Leemos los ficheros de logs

line_parser = apache_log_parser.make_parser("%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"")

def isTOR(ip):
#desechando esta funcion. Tarda mucho en buscar dentro de ficheros
    url = 'https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=1.1.1.1'

    try:
        TORfile=open("TOR.txt","w")
    except Exception as e:
        print ("Algo fue mal: ",e)

    respuesta = urllib2.urlopen(url)
    TORfile.write(respuesta.read())
    TORfile.close()

    TORfile=open("TOR.txt","r")
    for line in TORfile:
        if ip==line.strip('\n'):
            return True
    TORfile.close()


def listtorip():
    url = 'https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=1.1.1.1'

    try:
        TORfile = open("TOR.txt", "w")
    except Exception as e:
        print ("Algo fue mal: ", e)

    respuesta = urllib2.urlopen(url)
    TORfile.write(respuesta.read())
    TORfile.close()

    TORfile = open("TOR.txt", "r")
    listaips=[]
    for line in TORfile:
        if line[0]!="#":
            listaips.append(line.strip('\n'))

    return listaips
    TORfile.close()

TORIP = listtorip()

try:
    fileaccess=open("access_log.processed", "r")
except Exception as e:
    print("Algo fue mal: ", e)




for line in fileaccess:
    try:
        TORIP.index(line_parser(line)["remote_host"])
    except ValueError:
        "Do Nothing"
    else:
        print line

fileaccess.close()



"""

print "Ahora toca error_log"
try:
    fileerror=open("error_log", "r")
except Exception as e:
    print("Algo fue mal: ", e)

for line in fileerror:
    if line.find("[client")!=-1:
        inicio_campo = line.find("[client")
        fin_campo = line.find("]", inicio_campo)
        dos_puntos = line.find(":", inicio_campo, fin_campo)
        if dos_puntos!=-1:
            inicio_ip=inicio_campo+8
#            print line[inicio_ip:dos_puntos]
            ip=line[inicio_ip:dos_puntos]
            try:
                TORIP.index(ip)
            except ValueError:
                "Do nothing"
            else:
                print line
#        print line.find("[client")
#        print line.find("]",36)
#        print line.find(":",36,line.find("]",36))




fileerror.close()
"""