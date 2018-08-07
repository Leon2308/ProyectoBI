# ProyectoBI

PROYECTO FINAL INTELIGENCIA DE NEGOCIOS

Participantes
-Pilatuña Isaac

-Sandoval Leonardo


Método

1.- Adquisición de datos:

Primero se tuvo que hacer la recolección de datos en las fechas del mundial asignadas a cada grupo, para lo cual se determinó un dia, hora y partido(s).
La recolección se lo realizó mediante un script en Python y fueron almacenados en una base de datos CouchDB. 

2.- Preprocesamiento:

Luego se procede a filtrar los tweets (emojis, caracteres especiales, tags) y a elegir los campos a analizar. Esto se lo realizó en una vista que está adjunta
al proyecto. En este caso se realizó los filtro sin importar el idioma pues posteriormente se traducirán los tweets al idioma inglés para proceder con el procesamiento 
de la información.

Así mismo en esta fase se realizó el filtrado para obtener solo tweets del mundial, mediante los hashtags oficiales del mundial, entre los que se tiene principalme: 
#WorldCup, #Rusia2018, #RUS, #russia2018, entre otros. A estos hashtags es necesario agregar los que corresponden a cada pais por cada partido.

3.- Procesamiento:
Una vez procesados los filtrados los tweets, se procede con el procesamiento, específicamente del campo texto para poder determinar la opinión pública respecto al 
sentimiento respecto al mundial. Para poder realizar este procesamiento con la herramienta textBlob, fue necesario traducir los tweets a inglés, lo cual se lo realizó
con la herramienta googletrans.

4. Análisis:

En esta fase se procedió a realizar el análisis de las siguiente forma:
• Tweets por hora del día, lo cual se verá reflejado en una gráfico de barras.
• Tweets por fecha, lo cual se verá reflejado en una gráfico de barras. 
• Tweets por idioma, lo cual se verá reflejado en una gráfico de barras.
• Porcentaje de sentimientos, lo cual se verá reflejado en una gráfico de pastel.
• Tweets por país, lo cual se verá reflejado en una gráfico de barras.
y finalmente para los tweets relacionados al mundial por país.


•Resultados

Se obtuvieron los resultados esperados, los cuales se pueden ver reflejados mediante: 
-Gráficos de barras para los tweets por hora en el cual se puede observar, que la mayor cantidad de tweets se generan en las horas del partido
-Gráficos de barras para los tweets por idioma en donde prevalece el idioma del país o de los paises que jugaron. Sin embargo el también hay varios tweets
 que se los realizan en inglés.
-Gráfico pastel para el porcentaje de sentimientos, en el cual la mayoria de tweets están en el rango neutro, seguido de positivo y por último negativo.


•Conclusiones y trabajo futuro

- TextBlob es una biblioteca que funciona en Python y permite realizar tareas de procesamiento del lenguaje natural, tal como análisis de sentimientos, 
clasificación de datos, entre otros.

- El analisis de los sentimientos se lo realizó con la herramienta textBlob, analizando primero la polaridad y dependiendo de esta clasificando por neutro, positivo 
y negativo. Asi mismo se lo puede realizar mediante datos de entrenamiento, para lo cual se los debe etiquetar y para comprobar lo se genera un conjunto de datos 
para prueba. 

- Para mostrar los resultados gráficamente se utilizó Matplotlib es una biblioteca para la generación de gráficos a partir de datos contenidos en listas o arrays en 
el lenguaje de programación Python.

- La cantidad de tweets generados durante la hora que se juega un partido es mayor que en otras horas.

- Seria interesante tener otra forma de obtener las coordenas de ubicación desde donde se realiza un tweets, hacerlo automáticamente para poder obtener una mejor 
descripción de los lugares en los que se generan la mayor cantidad de tweets. 


•Apéndice: instrucciones de instalación y funcionamiento

Para la recolección de datos se utilizó el gestor base de datos de código abierto, couchDB, se ejecuta:
apt-get install couchdb

Para la generación de scripts se lo realiza en Python, se ejecuta:
apt-get install python.pip

Para el análisis de sentimientos se lo realiza con la herramiento para procesar texto textblob, se ejecuta:
pip install -u textblob

Para la traducción de tweets es necesario importar la libreria:
from googletrans import Translator 

Finalmente para los gráficos de barras, pasteles se lo realizó mediante la libreria Pylab, Matplotlib. y Kinder
pip install matplotlib
pip install Kinder
