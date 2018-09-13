# -*- coding: utf-8 -*-
pilha = []
caminho = ''

class Grafo():
	
	def __init__(self):
		self.viz = {}
		self.cores = {}
		self.pred = {}
		

def visita(G,u,a,i):

	G.cores[u] = "cinza"
	pilha.append(u)
	#print(pilha)

	for x in G.viz[u]:
		if G.cores[x] == "branco":
			visita(G,x,a,i)

			if pilha[0] == a and pilha[-1] == i:

				for i in pilha:
					global caminho
					caminho = caminho +i+" "
			

			pilha.pop()
	return True
		
def profundidade(G,a,i):

	#print("Vizinhança atual",G.viz)
	for x in G.viz:
		if G.cores[x] == "branco":
			if visita(G,x,a,i):
				break
			
	print(caminho)

def main():

	listaAux	 = []
	arquivo = open("entrada2.txt","+r")
	linhas = arquivo.read().splitlines()
	A = linhas[0]
	I = linhas[1]

	#print("A:",A)
	#print("I:",I)

	G = Grafo()

	#gerando lista de adjacencia
	for x in linhas[2:]:
		listaAux = x.split(" ")
		G.viz[listaAux[0]] = listaAux[1:]

	#G.viz = sorted(G.viz.items(), key=lambda t:t[0])
	#print(G.viz)

	#print(G.viz.keys())
	#pinta cada vertice de branco

	for v in G.viz.keys():
		G.cores[v] = "branco"

	#print(G.cores)

	profundidade(G,A,I)

if __name__ == '__main__':
	main()	
