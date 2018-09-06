import sys

G = {}
listaAux = []
dist = {}
cores = {}
fila = []
pred = {}

arquivo = open("entrada.txt","+r")

linhas = arquivo.read().splitlines()


def main():

	#gerando lista de adjacencia
	for x in linhas:
		listaAux = x.split(" ")
		G[listaAux[0]] = listaAux[1:] 
		
	for x in G:
		if x != "A":
			dist[x] = 0
			cores[x] = "branca"

	dist["A"] = 0
	cores["A"] = "azul"
	pred["A"] = None
	fila.append("A")

	#print("Grafo")
	#print(G)
	#print("Distancia")
	#print(dist)
	#print("Cores")
	#print(cores)
	#print(fila)

	while len(fila) > 0:
		u = fila[0]
		for v in G[u]:
			if cores[v] == "branca": # vertice nunca foi visitado
				cores[v] = "azul"
				dist[v] = dist[u] + 1
				pred[v] = u # seta predecessor de um vertice
				fila.append(v)
		h = input("Para")
		
		#desenfila
		fila.pop(0)

		cores[u] = "azul"


	print(dist)
	
if __name__ == '__main__':
	main()
