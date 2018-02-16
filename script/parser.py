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
robots = robots.replace("Sitemap", "sitemap")
count_sitemap = robots.count("sitemap")


#Verifica se existe Sitemap no Robots.txt
#ESQUEMA PARA LER 1 SITEMAP, TERIA QUE OTIMIZAR PARA MAIS DE 1
sitemap_urls = []

if 'sitemap' in robots:
	s = robots.split("sitemap: ")
	sitemap_urls.append(s[1])
else:
	print "Não há Sitemap"
	exit()




#----Sitemap

all_urls = []


for i in range(0, len(sitemap_urls)):
	#Visita página do sitemap e recupera links
	try:
		response = urllib2.urlopen(sitemap_urls[i])
	except urllib2.URLError, e:
	    print 'Não foi possível acessar o \"Sitemap\". Código de erro', e
	    exit()	
	

	sitemap = response.read()
	urls = sitemap.split("<loc>")	

	for i in range(1,len(urls)):
		urls[i] = urls[i].split("</loc>")[0]	

	del urls[0] #lista urls contém todos os links do sitemap	



all_urls.append(urls);

#imprimir
for i in range(0, len(all_urls)):
	for j in range (0, len(all_urls[i])):
		print all_urls[i][j]	