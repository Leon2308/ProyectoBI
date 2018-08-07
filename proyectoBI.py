
import couchdb
import sys
import urllib2
import json
from textblob import TextBlob
from googletrans import Translator
from couchdb import view
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly.graph_objs as go

contador=0
limite=50000
positivosCOLvsENG=0
negativosCOLvsENG=0
neutrosCOLvsENG=0
positivosSUEvsSUI=0
negativosSUEvsSUI=0
neutrosSUEvsSUI=0
positivosBELvsENG=0
negativosBELvsENG=0
neutrosBELvsENG=0
positivosFRAvsCRO=0
negativosFRAvsCRO=0
neutrosFRAvsCRO=0
positivos=0
negativos=0
neutros=0
horasCOLvsENG=[]
conteoPorHorasCOLvsENG=[]
horasSUEvsSUI=[]
conteoPorHorasSUEvsSUI=[]
horasBELvsENG=[]
conteoPorHorasBELvsENG=[]
horasFRAvsCRO=[]
conteoPorHorasFRAvsCRO=[]
lenguajes=[]
conteoLenguajes=[]
lenguajesCOLvsENG=[]
conteoLenguajesCOLvsENG=[]
lenguajesSUEvsSUI=[]
conteoLenguajesSUEvsSUI=[]
lenguajesBELvsENG=[]
conteoLenguajesBELvsENG=[]
lenguajesFRAvsCRO=[]
conteoLenguajesFRAvsCRO=[]
paises=[]
conteoPaises=[]
paisesCOLvsENG=[]
conteoPaisesCOLvsENG=[]
paisesSUEvsSUI=[]
conteoPaisesSUEvsSUI=[]
paisesBELvsENG=[]
conteoPaisesBELvsENG=[]
paisesFRAvsCRO=[]
conteoPaisesFRAvsCRO=[]
fechas=[]
conteoFechas=[]



'''
 COLOMBIA
==============
'''

URL = 'localhost'
db_name = 'colombia'

traductor = Translator()

'''========couchdb'=========='''
server = couchdb.Server('http://'+URL+':5984/')  
try:
    print db_name
    db = server[db_name]
    print 'success'

except:
    sys.stderr.write("Error: DB not found. Closing...\n")
    sys.exit()



url = 'http://127.0.0.1:5984/colombia/_design/colombiaMundial/_view/colombiaMundial'
req = urllib2.Request(url)
f = urllib2.urlopen(req)
d = json.loads(f.read())
contadorColombia=0
for x in d['rows']:
	contador=contador+1
	fechaCompleta=x['value']['fecha']
	fecha=fechaCompleta.split()[2]+" "+fechaCompleta.split()[1]+" "+fechaCompleta.split()[5]
	if(fecha=='03 Jul 2018'):
		contadorColombia=contadorColombia+1
		texto=x['value']['texto']
		textoTraducido = traductor.translate(texto,'en').text
		polaridad=TextBlob(textoTraducido).sentiment.polarity
		if(polaridad>0):
			positivos=positivos+1
			positivosCOLvsENG=positivosCOLvsENG+1
		if(polaridad==0):
			neutros=neutros+1
			neutrosCOLvsENG=neutrosCOLvsENG+1
		if(polaridad<0):
			negativosCOLvsENG=negativosCOLvsENG+1
			negativos=negativos+1
		hora=fechaCompleta.split()[3].split(':')[0]
		if hora in horasCOLvsENG:
			indice=horasCOLvsENG.index(hora)
			conteoPorHorasCOLvsENG[indice]=conteoPorHorasCOLvsENG[indice]+1
		else:
			horasCOLvsENG.append(hora)
			conteoPorHorasCOLvsENG.append(1)
		lenguaje=x['value']['lenguaje']
		if lenguaje in lenguajesCOLvsENG:
			indice=lenguajesCOLvsENG.index(lenguaje)
			conteoLenguajesCOLvsENG[indice]=conteoLenguajesCOLvsENG[indice]+1
		else:
			lenguajesCOLvsENG.append(lenguaje)
			conteoLenguajesCOLvsENG.append(1)
		if lenguaje in lenguajes:
			indice=lenguajes.index(lenguaje)
			conteoLenguajes[indice]=conteoLenguajes[indice]+1
		else:
			lenguajes.append(lenguaje)
			conteoLenguajes.append(1)
		pais=x['value']['pais']
		if pais in paisesCOLvsENG:
			indice=paisesCOLvsENG.index(pais)
			conteoPaisesCOLvsENG[indice]=conteoPaisesCOLvsENG[indice]+1
		else:
			paisesCOLvsENG.append(pais)
			conteoPaisesCOLvsENG.append(1)
		if pais in paises:
			indice=paises.index(pais)
			conteoPaises[indice]=conteoPaises[indice]+1
		else:
			paises.append(pais)
			conteoPaises.append(1)
		if fecha in fechas:
			indice=fechas.index(fecha)
			conteoFechas[indice]=conteoFechas[indice]+1
		else:
			fechas.append(fecha)
			conteoFechas.append(1)
		if(contadorColombia>limite):
			break

'''
 INGLATERRA
==============
'''

URL = 'localhost'
db_name = 'inglaterra'

traductor = Translator()

'''========couchdb'=========='''
server = couchdb.Server('http://'+URL+':5984/')  
try:
    print db_name
    db = server[db_name]
    print 'success'

except:
    sys.stderr.write("Error: DB not found. Closing...\n")
    sys.exit()



url = 'http://127.0.0.1:5984/inglaterra/_design/inglaterraMundial/_view/inglaterraMundial'
req = urllib2.Request(url)
f = urllib2.urlopen(req)
d = json.loads(f.read())
contadorIngVsCol=0
contadorIngvsBel=0
for x in d['rows']:
	contador=contador+1
	fechaCompleta=x['value']['fecha']
	fecha=fechaCompleta.split()[2]+" "+fechaCompleta.split()[1]+" "+fechaCompleta.split()[5]
	if(contadorIngVsCol<limite):
		if(fecha=='03 Jul 2018'):
			contadorIngVsCol=contadorIngVsCol+1
			texto=x['value']['texto']
			textoTraducido = traductor.translate(texto,'en').text
			polaridad=TextBlob(textoTraducido).sentiment.polarity
			if(polaridad>0):
				positivos=positivos+1
				positivosCOLvsENG=positivosCOLvsENG+1
			if(polaridad==0):
				neutros=neutros+1
				neutrosCOLvsENG=neutrosCOLvsENG+1
			if(polaridad<0):
				negativosCOLvsENG=negativosCOLvsENG+1
				negativos=negativos+1
			hora=fechaCompleta.split()[3].split(':')[0]
			if hora in horasCOLvsENG:
				indice=horasCOLvsENG.index(hora)
				conteoPorHorasCOLvsENG[indice]=conteoPorHorasCOLvsENG[indice]+1
			else:
				horasCOLvsENG.append(hora)
				conteoPorHorasCOLvsENG.append(1)
			lenguaje=x['value']['lenguaje']
			if lenguaje in lenguajesCOLvsENG:
				indice=lenguajesCOLvsENG.index(lenguaje)
				conteoLenguajesCOLvsENG[indice]=conteoLenguajesCOLvsENG[indice]+1
			else:
				lenguajesCOLvsENG.append(lenguaje)
				conteoLenguajesCOLvsENG.append(1)
			if lenguaje in lenguajes:
				indice=lenguajes.index(lenguaje)
				conteoLenguajes[indice]=conteoLenguajes[indice]+1
			else:
				lenguajes.append(lenguaje)
				conteoLenguajes.append(1)
			pais=x['value']['pais']
			if pais in paisesCOLvsENG:
				indice=paisesCOLvsENG.index(pais)
				conteoPaisesCOLvsENG[indice]=conteoPaisesCOLvsENG[indice]+1
			else:
				paisesCOLvsENG.append(pais)
				conteoPaisesCOLvsENG.append(1)
			if pais in paises:
				indice=paises.index(pais)
				conteoPaises[indice]=conteoPaises[indice]+1
			else:
				paises.append(pais)
				conteoPaises.append(1)
			if fecha in fechas:
				indice=fechas.index(fecha)
				conteoFechas[indice]=conteoFechas[indice]+1
			else:
				fechas.append(fecha)
				conteoFechas.append(1)
	if(fecha=='14 Jul 2018'):
		contadorIngvsBel=contadorIngvsBel+1
		texto=x['value']['texto']
		textoTraducido = traductor.translate(texto,'en').text
		polaridad=TextBlob(textoTraducido).sentiment.polarity
		if(polaridad>0):
			positivos=positivos+1
			positivosBELvsENG=positivosBELvsENG+1
		if(polaridad==0):
			neutros=neutros+1
			neutrosBELvsENG=neutrosBELvsENG+1
		if(polaridad<0):
			negativosBELvsENG=negativosBELvsENG+1
			negativos=negativos+1
		hora=fechaCompleta.split()[3].split(':')[0]
		if hora in horasBELvsENG:
			indice=horasBELvsENG.index(hora)
			conteoPorHorasBELvsENG[indice]=conteoPorHorasBELvsENG[indice]+1
		else:
			horasBELvsENG.append(hora)
			conteoPorHorasBELvsENG.append(1)
		lenguaje=x['value']['lenguaje']
		if lenguaje in lenguajesBELvsENG:
			indice=lenguajesBELvsENG.index(lenguaje)
			conteoLenguajesBELvsENG[indice]=conteoLenguajesBELvsENG[indice]+1
		else:
			lenguajesBELvsENG.append(lenguaje)
			conteoLenguajesBELvsENG.append(1)
		if lenguaje in lenguajes:
			indice=lenguajes.index(lenguaje)
			conteoLenguajes[indice]=conteoLenguajes[indice]+1
		else:
			lenguajes.append(lenguaje)
			conteoLenguajes.append(1)
		pais=x['value']['pais']
		if pais in paisesBELvsENG:
			indice=paisesBELvsENG.index(pais)
			conteoPaisesBELvsENG[indice]=conteoPaisesBELvsENG[indice]+1
		else:
			paisesBELvsENG.append(pais)
			conteoPaisesBELvsENG.append(1)
		if pais in paises:
			indice=paises.index(pais)
			conteoPaises[indice]=conteoPaises[indice]+1
		else:
			paises.append(pais)
			conteoPaises.append(1)
		if fecha in fechas:
			indice=fechas.index(fecha)
			conteoFechas[indice]=conteoFechas[indice]+1
		else:
			fechas.append(fecha)
			conteoFechas.append(1)
		if(contadorIngvsBel>limite):
			break

'''
 SUECIA
==============
'''

URL = 'localhost'
db_name = 'suecia'

traductor = Translator()

'''========couchdb'=========='''
server = couchdb.Server('http://'+URL+':5984/')  
try:
    print db_name
    db = server[db_name]
    print 'success'

except:
    sys.stderr.write("Error: DB not found. Closing...\n")
    sys.exit()



url = 'http://127.0.0.1:5984/suecia/_design/sueciamundial/_view/sueciaMundial'
req = urllib2.Request(url)
f = urllib2.urlopen(req)
d = json.loads(f.read())
contadorSuecia=0
for x in d['rows']:
	fechaCompleta=x['value']['fecha']
	fecha=fechaCompleta.split()[2]+" "+fechaCompleta.split()[1]+" "+fechaCompleta.split()[5]
	if(fecha=='03 Jul 2018'):
		contadorSuecia=contadorSuecia+1
		texto=x['value']['texto']
		textoTraducido = traductor.translate(texto,'en').text
		polaridad=TextBlob(textoTraducido).sentiment.polarity
		contador=contador+1
		if(polaridad>0):
			positivos=positivos+1
			positivosSUEvsSUI=positivosSUEvsSUI+1
		if(polaridad==0):
			neutros=neutros+1
			neutrosSUEvsSUI=neutrosSUEvsSUI+1
		if(polaridad<0):
			negativosSUEvsSUI=negativosSUEvsSUI+1
			negativos=negativos+1
		hora=fechaCompleta.split()[3].split(':')[0]
		if hora in horasSUEvsSUI:
			indice=horasSUEvsSUI.index(hora)
			conteoPorHorasSUEvsSUI[indice]=conteoPorHorasSUEvsSUI[indice]+1
		else:
			horasSUEvsSUI.append(hora)
			conteoPorHorasSUEvsSUI.append(1)
		lenguaje=x['value']['lenguaje']
		if lenguaje in lenguajesSUEvsSUI:
			indice=lenguajesSUEvsSUI.index(lenguaje)
			conteoLenguajesSUEvsSUI[indice]=conteoLenguajesSUEvsSUI[indice]+1
		else:
			lenguajesSUEvsSUI.append(lenguaje)
			conteoLenguajesSUEvsSUI.append(1)
		if lenguaje in lenguajes:
			indice=lenguajes.index(lenguaje)
			conteoLenguajes[indice]=conteoLenguajes[indice]+1
		else:
			lenguajes.append(lenguaje)
			conteoLenguajes.append(1)
		pais=x['value']['pais']
		if pais in paisesSUEvsSUI:
			indice=paisesSUEvsSUI.index(pais)
			conteoPaisesSUEvsSUI[indice]=conteoPaisesSUEvsSUI[indice]+1
		else:
			paisesSUEvsSUI.append(pais)
			conteoPaisesSUEvsSUI.append(1)
		if pais in paises:
			indice=paises.index(pais)
			conteoPaises[indice]=conteoPaises[indice]+1
		else:
			paises.append(pais)
			conteoPaises.append(1)
		if fecha in fechas:
			indice=fechas.index(fecha)
			conteoFechas[indice]=conteoFechas[indice]+1
		else:
			fechas.append(fecha)
			conteoFechas.append(1)
		if(contadorSuecia>limite):
			break

'''
 SUIZA
==============
'''

URL = 'localhost'
db_name = 'suiza'

traductor = Translator()

'''========couchdb'=========='''
server = couchdb.Server('http://'+URL+':5984/')  
try:
    print db_name
    db = server[db_name]
    print 'success'

except:
    sys.stderr.write("Error: DB not found. Closing...\n")
    sys.exit()



url = 'http://127.0.0.1:5984/suiza/_design/suizaMundial/_view/suizaMundial'
req = urllib2.Request(url)
f = urllib2.urlopen(req)
d = json.loads(f.read())
contadorSuiza=0
for x in d['rows']:
	fechaCompleta=x['value']['fecha']
	fecha=fechaCompleta.split()[2]+" "+fechaCompleta.split()[1]+" "+fechaCompleta.split()[5]
	if(fecha=='03 Jul 2018'):
		contadorSuiza=contadorSuiza+1
		texto=x['value']['texto']
		textoTraducido = traductor.translate(texto,'en').text
		polaridad=TextBlob(textoTraducido).sentiment.polarity
		contador=contador+1
		if(polaridad>0):
			positivos=positivos+1
			positivosSUEvsSUI=positivosSUEvsSUI+1
		if(polaridad==0):
			neutros=neutros+1
			neutrosSUEvsSUI=neutrosSUEvsSUI+1
		if(polaridad<0):
			negativosSUEvsSUI=negativosSUEvsSUI+1
			negativos=negativos+1
		hora=fechaCompleta.split()[3].split(':')[0]
		if hora in horasSUEvsSUI:
			indice=horasSUEvsSUI.index(hora)
			conteoPorHorasSUEvsSUI[indice]=conteoPorHorasSUEvsSUI[indice]+1
		else:
			horasSUEvsSUI.append(hora)
			conteoPorHorasSUEvsSUI.append(1)
		lenguaje=x['value']['lenguaje']
		if lenguaje in lenguajesSUEvsSUI:
			indice=lenguajesSUEvsSUI.index(lenguaje)
			conteoLenguajesSUEvsSUI[indice]=conteoLenguajesSUEvsSUI[indice]+1
		else:
			lenguajesSUEvsSUI.append(lenguaje)
			conteoLenguajesSUEvsSUI.append(1)
		if lenguaje in lenguajes:
			indice=lenguajes.index(lenguaje)
			conteoLenguajes[indice]=conteoLenguajes[indice]+1
		else:
			lenguajes.append(lenguaje)
			conteoLenguajes.append(1)
		pais=x['value']['pais']
		if pais in paisesSUEvsSUI:
			indice=paisesSUEvsSUI.index(pais)
			conteoPaisesSUEvsSUI[indice]=conteoPaisesSUEvsSUI[indice]+1
		else:
			paisesSUEvsSUI.append(pais)
			conteoPaisesSUEvsSUI.append(1)
		if pais in paises:
			indice=paises.index(pais)
			conteoPaises[indice]=conteoPaises[indice]+1
		else:
			paises.append(pais)
			conteoPaises.append(1)
		if fecha in fechas:
			indice=fechas.index(fecha)
			conteoFechas[indice]=conteoFechas[indice]+1
		else:
			fechas.append(fecha)
			conteoFechas.append(1)
		if(contadorSuiza>limite):
			break

'''
 BELGICA
==============
'''

URL = 'localhost'
db_name = 'belgica'

traductor = Translator()

'''========couchdb'=========='''
server = couchdb.Server('http://'+URL+':5984/')  
try:
    print db_name
    db = server[db_name]
    print 'success'

except:
    sys.stderr.write("Error: DB not found. Closing...\n")
    sys.exit()



url = 'http://127.0.0.1:5984/belgica/_design/belgicaMundial/_view/belgicaMundial'
req = urllib2.Request(url)
f = urllib2.urlopen(req)
d = json.loads(f.read())
contadorBelg=0
for x in d['rows']:
	fechaCompleta=x['value']['fecha']
	fecha=fechaCompleta.split()[2]+" "+fechaCompleta.split()[1]+" "+fechaCompleta.split()[5]
	if(fecha=='14 Jul 2018'):
		contadorBelg=contadorBelg+1
		texto=x['value']['texto']
		textoTraducido = traductor.translate(texto,'en').text
		polaridad=TextBlob(textoTraducido).sentiment.polarity
		if(polaridad>0):
			positivos=positivos+1
			positivosBELvsENG=positivosBELvsENG+1
		if(polaridad==0):
			neutros=neutros+1
			neutrosBELvsENG=neutrosBELvsENG+1
		if(polaridad<0):
			negativosBELvsENG=negativosBELvsENG+1
			negativos=negativos+1
		hora=fechaCompleta.split()[3].split(':')[0]
		if hora in horasBELvsENG:
			indice=horasBELvsENG.index(hora)
			conteoPorHorasBELvsENG[indice]=conteoPorHorasBELvsENG[indice]+1
		else:
			horasBELvsENG.append(hora)
			conteoPorHorasBELvsENG.append(1)
		lenguaje=x['value']['lenguaje']
		if lenguaje in lenguajesBELvsENG:
			indice=lenguajesBELvsENG.index(lenguaje)
			conteoLenguajesBELvsENG[indice]=conteoLenguajesBELvsENG[indice]+1
		else:
			lenguajesBELvsENG.append(lenguaje)
			conteoLenguajesBELvsENG.append(1)
		if lenguaje in lenguajes:
			indice=lenguajes.index(lenguaje)
			conteoLenguajes[indice]=conteoLenguajes[indice]+1
		else:
			lenguajes.append(lenguaje)
			conteoLenguajes.append(1)
		pais=x['value']['pais']
		if pais in paisesBELvsENG:
			indice=paisesBELvsENG.index(pais)
			conteoPaisesBELvsENG[indice]=conteoPaisesBELvsENG[indice]+1
		else:
			paisesBELvsENG.append(pais)
			conteoPaisesBELvsENG.append(1)
		if pais in paises:
			indice=paises.index(pais)
			conteoPaises[indice]=conteoPaises[indice]+1
		else:
			paises.append(pais)
			conteoPaises.append(1)
		if fecha in fechas:
			indice=fechas.index(fecha)
			conteoFechas[indice]=conteoFechas[indice]+1
		else:
			fechas.append(fecha)
			conteoFechas.append(1)
		if(contadorBelg>limite):
			break

'''
 FRANCIA
==============
'''

URL = 'localhost'
db_name = 'francia'

traductor = Translator()

'''========couchdb'=========='''
server = couchdb.Server('http://'+URL+':5984/')  
try:
    print db_name
    db = server[db_name]
    print 'success'

except:
    sys.stderr.write("Error: DB not found. Closing...\n")
    sys.exit()



url = 'http://127.0.0.1:5984/francia/_design/franciaMundial/_view/franciaMundial'
req = urllib2.Request(url)
f = urllib2.urlopen(req)
d = json.loads(f.read())
contadorFr=0
for x in d['rows']:
	fechaCompleta=x['value']['fecha']
	fecha=fechaCompleta.split()[2]+" "+fechaCompleta.split()[1]+" "+fechaCompleta.split()[5]
	if(fecha=='15 Jul 2018'):
		contadorFr=contadorFr+1
		texto=x['value']['texto']
		textoTraducido = traductor.translate(texto,'en').text
		polaridad=TextBlob(textoTraducido).sentiment.polarity
		if(polaridad>0):
			positivos=positivos+1
			positivosFRAvsCRO=positivosFRAvsCRO+1
		if(polaridad==0):
			neutros=neutros+1
			neutrosFRAvsCRO=neutrosFRAvsCRO+1
		if(polaridad<0):
			negativosFRAvsCRO=negativosFRAvsCRO+1
			negativos=negativos+1
		hora=fechaCompleta.split()[3].split(':')[0]
		if hora in horasFRAvsCRO:
			indice=horasFRAvsCRO.index(hora)
			conteoPorHorasFRAvsCRO[indice]=conteoPorHorasFRAvsCRO[indice]+1
		else:
			horasFRAvsCRO.append(hora)
			conteoPorHorasFRAvsCRO.append(1)
		lenguaje=x['value']['lenguaje']
		if lenguaje in lenguajesFRAvsCRO:
			indice=lenguajesFRAvsCRO.index(lenguaje)
			conteoLenguajesFRAvsCRO[indice]=conteoLenguajesFRAvsCRO[indice]+1
		else:
			lenguajesFRAvsCRO.append(lenguaje)
			conteoLenguajesFRAvsCRO.append(1)
		if lenguaje in lenguajes:
			indice=lenguajes.index(lenguaje)
			conteoLenguajes[indice]=conteoLenguajes[indice]+1
		else:
			lenguajes.append(lenguaje)
			conteoLenguajes.append(1)
		pais=x['value']['pais']
		if pais in paisesFRAvsCRO:
			indice=paisesFRAvsCRO.index(pais)
			conteoPaisesFRAvsCRO[indice]=conteoPaisesFRAvsCRO[indice]+1
		else:
			paisesFRAvsCRO.append(pais)
			conteoPaisesFRAvsCRO.append(1)
		if pais in paises:
			indice=paises.index(pais)
			conteoPaises[indice]=conteoPaises[indice]+1
		else:
			paises.append(pais)
			conteoPaises.append(1)
		if fecha in fechas:
			indice=fechas.index(fecha)
			conteoFechas[indice]=conteoFechas[indice]+1
		else:
			fechas.append(fecha)
			conteoFechas.append(1)
		if(contadorFr>limite):
			break
		
'''
 CROACIA
==============
'''

URL = 'localhost'
db_name = 'croacia'

traductor = Translator()

'''========couchdb'=========='''
server = couchdb.Server('http://'+URL+':5984/')  
try:
    print db_name
    db = server[db_name]
    print 'success'

except:
    sys.stderr.write("Error: DB not found. Closing...\n")
    sys.exit()



url = 'http://127.0.0.1:5984/croacia/_design/croaciaMundial/_view/croaciaMundial'
req = urllib2.Request(url)
f = urllib2.urlopen(req)
d = json.loads(f.read())
contadorcr=0
for x in d['rows']:
	fechaCompleta=x['value']['fecha']
	fecha=fechaCompleta.split()[2]+" "+fechaCompleta.split()[1]+" "+fechaCompleta.split()[5]
	if(fecha=='15 Jul 2018'):
		contadorcr=contadorcr+1
		texto=x['value']['texto']
		textoTraducido = traductor.translate(texto,'en').text
		polaridad=TextBlob(textoTraducido).sentiment.polarity
		if(polaridad>0):
			positivos=positivos+1
			positivosFRAvsCRO=positivosFRAvsCRO+1
		if(polaridad==0):
			neutros=neutros+1
			neutrosFRAvsCRO=neutrosFRAvsCRO+1
		if(polaridad<0):
			negativosFRAvsCRO=negativosFRAvsCRO+1
			negativos=negativos+1
		hora=fechaCompleta.split()[3].split(':')[0]
		if hora in horasFRAvsCRO:
			indice=horasFRAvsCRO.index(hora)
			conteoPorHorasFRAvsCRO[indice]=conteoPorHorasFRAvsCRO[indice]+1
		else:
			horasFRAvsCRO.append(hora)
			conteoPorHorasFRAvsCRO.append(1)
		lenguaje=x['value']['lenguaje']
		if lenguaje in lenguajesFRAvsCRO:
			indice=lenguajesFRAvsCRO.index(lenguaje)
			conteoLenguajesFRAvsCRO[indice]=conteoLenguajesFRAvsCRO[indice]+1
		else:
			lenguajesFRAvsCRO.append(lenguaje)
			conteoLenguajesFRAvsCRO.append(1)
		if lenguaje in lenguajes:
			indice=lenguajes.index(lenguaje)
			conteoLenguajes[indice]=conteoLenguajes[indice]+1
		else:
			lenguajes.append(lenguaje)
			conteoLenguajes.append(1)
		pais=x['value']['pais']
		if pais in paisesFRAvsCRO:
			indice=paisesFRAvsCRO.index(pais)
			conteoPaisesFRAvsCRO[indice]=conteoPaisesFRAvsCRO[indice]+1
		else:
			paisesFRAvsCRO.append(pais)
			conteoPaisesFRAvsCRO.append(1)
		if pais in paises:
			indice=paises.index(pais)
			conteoPaises[indice]=conteoPaises[indice]+1
		else:
			paises.append(pais)
			conteoPaises.append(1)
		if fecha in fechas:
			indice=fechas.index(fecha)
			conteoFechas[indice]=conteoFechas[indice]+1
		else:
			fechas.append(fecha)
			conteoFechas.append(1)
		if(contadorcr>limite):
			break

'''
GRAFICA COLOMBIA VS INGLATERRA
'''
ancho =1/1.5
plt.subplot(221)
plt.bar(horasCOLvsENG,conteoPorHorasCOLvsENG, ancho, color='gold')
plt.title('Tweets Por Hora del Dia')
plt.ylabel('Tweets')
plt.xlabel('Hora del Dia')
plt.suptitle('ANALISIS DE COLOMBIA VS INGLATERRA')

plt.subplot(222)
plt.bar(lenguajesCOLvsENG,conteoLenguajesCOLvsENG, ancho, color='lightskyblue')
plt.title('Tweets Por Idioma')
plt.ylabel('Idiomas')
plt.xlabel('Tweets')

plt.subplot(223)
plt.bar(paisesCOLvsENG,conteoPaisesCOLvsENG, ancho, color='lightcoral')
plt.title('Tweets Por Paises')
plt.ylabel('Paises')
plt.xlabel('Tweets')

etiquetas=['Positivos','Negativos','Neutros']
tamanio=[positivosCOLvsENG,negativosCOLvsENG,neutrosCOLvsENG]
colores=['gold','lightskyblue','lightcoral']
plt.subplot(224)
plt.pie(tamanio,labels=etiquetas,colors=colores,shadow=True, startangle=90, autopct='%.1f%%')
plt.axis('equal')
plt.tight_layout()
fig=plt.gcf()
fig.savefig("COLvsENG.png")
plt.show()


'''
GRAFICA SUECIA VS SUIZA
'''
plt.subplot(221)
plt.bar(horasSUEvsSUI,conteoPorHorasSUEvsSUI, ancho, color='gold')
plt.title('Tweets Por Hora del Dia')
plt.ylabel('Tweets')
plt.xlabel('Hora del Dia')
plt.suptitle('ANALISIS DE SUECIA VS SUIZA')

plt.subplot(222)
plt.bar(lenguajesSUEvsSUI,conteoLenguajesSUEvsSUI, ancho, color='lightskyblue')
plt.title('Tweets Por Idioma')
plt.ylabel('Idiomas')
plt.xlabel('Tweets')

plt.subplot(223)
plt.bar(paisesSUEvsSUI,conteoPaisesSUEvsSUI, ancho, color='lightcoral')
plt.title('Tweets Por Paises')
plt.ylabel('Paises')
plt.xlabel('Tweets')

etiquetas=['Positivos','Negativos','Neutros']
tamanio=[positivosSUEvsSUI,negativosSUEvsSUI,neutrosSUEvsSUI]
colores=['gold','lightskyblue','lightcoral']
plt.subplot(224)
plt.pie(tamanio,labels=etiquetas,colors=colores,shadow=True, startangle=90, autopct='%.1f%%')
plt.axis('equal')
plt.tight_layout()
fig=plt.gcf()
fig.savefig("SWEvsSUI.png")
plt.show()


'''
GRAFICA BELGICA VS INGLATERRA
'''
plt.subplot(221)
plt.bar(horasBELvsENG,conteoPorHorasBELvsENG, ancho, color='gold')
plt.title('Tweets Por Hora del Dia')
plt.ylabel('Tweets')
plt.xlabel('Hora del Dia')
plt.suptitle('ANALISIS DE BELGICA VS INGLATERRA')

plt.subplot(222)
plt.bar(lenguajesBELvsENG,conteoLenguajesBELvsENG, ancho, color='lightskyblue')
plt.title('Tweets Por Idioma')
plt.ylabel('Idiomas')
plt.xlabel('Tweets')

plt.subplot(223)
plt.bar(paisesBELvsENG,conteoPaisesBELvsENG, ancho, color='lightcoral')
plt.title('Tweets Por Paises')
plt.ylabel('Paises')
plt.xlabel('Tweets')

etiquetas=['Positivos','Negativos','Neutros']
tamanio=[positivosBELvsENG,negativosBELvsENG,neutrosBELvsENG]
colores=['gold','lightskyblue','lightcoral']
plt.subplot(224)
plt.pie(tamanio,labels=etiquetas,colors=colores,shadow=True, startangle=90, autopct='%.1f%%')
plt.axis('equal')
plt.tight_layout()
fig=plt.gcf()
fig.savefig("BELvsENG.png")
plt.show()

'''
GRAFICA FRANCIA VS CROACIA
'''
plt.subplot(221)
plt.bar(horasFRAvsCRO,conteoPorHorasFRAvsCRO, ancho, color='gold')
plt.title('Tweets Por Hora del Dia')
plt.ylabel('Tweets')
plt.xlabel('Hora del Dia')
plt.suptitle('ANALISIS DE FRANCIA VS CROACIA')

plt.subplot(222)
plt.bar(lenguajesFRAvsCRO,conteoLenguajesFRAvsCRO, ancho, color='lightskyblue')
plt.title('Tweets Por Idioma')
plt.ylabel('Idiomas')
plt.xlabel('Tweets')

plt.subplot(223)
plt.bar(paisesFRAvsCRO,conteoPaisesFRAvsCRO, ancho, color='lightcoral')
plt.title('Tweets Por Paises')
plt.ylabel('Paises')
plt.xlabel('Tweets')

etiquetas=['Positivos','Negativos','Neutros']
tamanio=[positivosFRAvsCRO,negativosFRAvsCRO,neutrosFRAvsCRO]
colores=['gold','lightskyblue','lightcoral']
plt.subplot(224)
plt.pie(tamanio,labels=etiquetas,colors=colores,shadow=True, startangle=90, autopct='%.1f%%')
plt.axis('equal')
plt.tight_layout()
fig=plt.gcf()
fig.savefig("FRAvsCRO.png")
plt.show()

'''
GRAFICA GENERAL
'''
plt.subplot(221)
plt.bar(fechas,conteoFechas, ancho, color='gold')
plt.title('Tweets Por  Dia')
plt.ylabel('Tweets')
plt.xlabel('Dia')
plt.suptitle('ANALISIS GENERAL')

plt.subplot(222)
plt.bar(lenguajes,conteoLenguajes, ancho, color='lightskyblue')
plt.title('Tweets Por Idioma')
plt.ylabel('Idiomas')
plt.xlabel('Tweets')

plt.subplot(223)
plt.bar(paises,conteoPaises, ancho, color='lightcoral')
plt.title('Tweets Por Paises')
plt.ylabel('Paises')
plt.xlabel('Tweets')

etiquetas=['Positivos','Negativos','Neutros']
tamanio=[positivos,negativos,neutros]
colores=['gold','lightskyblue','lightcoral']
plt.subplot(224)
plt.pie(tamanio,labels=etiquetas,colors=colores,shadow=True, startangle=90, autopct='%.1f%%')
plt.axis('equal')
plt.tight_layout()
fig=plt.gcf()
fig.savefig("GENERAL.png")
plt.show()

