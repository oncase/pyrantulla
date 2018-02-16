#encoding: utf-8
import urllib2
import sys



#----Robots


parametro = sys.argv[1] #exemplo: 'http://www.cartoonnetwork.com.br/robots.txt'

#Verifica se dominio possui Robots.txt
try:
	response = urllib2.urlopen(parametro + "/robots.txt")
except urllib2.URLError, e:
    print 'Não foi possível acessar o \"Robots.txt\". Código de erro', e
    exit()

#Se houver robots, continua:
robots = response.read()

#Verifica se existe Sitemap no Robots.txt
#ESQUEMA PARA LER 1 SITEMAP, TERIA QUE OTIMIZAR PARA MAIS DE 1
if 'Sitemap' in robots:
	sitemap_url = robots.split("Sitemap: ")[1]
else:
	exit()




#----Sitemap


#Visita página do sitemap e recupera links
try:
	response = urllib2.urlopen(sitemap_url)
except urllib2.URLError, e:
    print 'Não foi possível acessar o \"Sitemap\". Código de erro', e
    exit()


sitemap = response.read()
urls = sitemap.split("<loc>")

for i in range(1,len(urls)):
	urls[i] = urls[i].split("</loc>")[0]

del urls[0] #lista urls contém todos os links do sitemap

#imprimir
for i in range(0, len(urls)):
	print urls[i]	