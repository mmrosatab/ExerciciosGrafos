import sys

G = {}
listaAux = []
dist = {}
cores = {}
fila = []
pred = {}

arquivo = open("entrada.txt","+r")

linhas = arquivo.read().splitlines()

def largura(G,s):

	for x in G:
		if x != s:
			dist[x] = 0
			cores[x] = "branca"

	dist[s] = 0
	cores[s] = "azul"
	pred[s] = None
	fila.append(s)

	while len(fila) > 0:

		u = fila[0]

		for v in G[u]:
			if cores[v] == "branca": # vertice nunca foi visitado
				cores[v] = "azul"
				dist[v] = dist[u] + 1
				pred[v] = u # seta predecessor de um vertice
				fila.append(v)
		
		
		
		fila.pop(0) #tira o primeiro vertice da fila

		cores[u] = "azul"

	for x in G:
		if x != s:
			print(s," ",x," ",dist[x])
	

def main():

	#gerando lista de adjacencia
	for x in linhas:
		listaAux = x.split(" ")
		G[listaAux[0]] = listaAux[1:] 
	
	largura(G,"A")

	#print(dist)
	
if __name__ == '__main__':
	main()