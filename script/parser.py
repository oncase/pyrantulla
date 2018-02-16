import urllib2

parametro = 'http://www.cartoonnetwork.com.br/robots.txt'
response = urllib2.urlopen(parametro)
robots = response.read()


#Verifica se existe Sitemap no Robots.txt
#ESQUEMA PARA LER 1 SITEMAP, TERIA QUE OTIMIZAR PARA MAIS DE 1
if 'Sitemap' in robots:
	sitemap_url = robots.split("Sitemap: ")[1]
	if sitemap_url.startswith("https"):
		sitemap_url = sitemap_url.split("\r")[0]
		print sitemap_url
else:
	exit()

#Visita pagina do sitemap e recupera links
response = urllib2.urlopen(sitemap_url)
sitemap = response.read()

urls = sitemap.split("<loc>")

for i in range(1,len(urls)):
	urls[i] = urls[i].split("</loc>")[0]

del urls[0]
print urls	#lista urls contem todos os links do sitemap