lAdj = {}
listaAux = []

arquivo = open("entrada.txt","+r")

linhas = arquivo.read().splitlines()

#gerando lista de adjacencia
for x in linhas:
	listaAux = x.split(" ")
	lAdj[listaAux[0]] = listaAux[1:] 


print(lAdj)