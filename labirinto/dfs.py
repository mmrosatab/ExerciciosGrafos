G = {}
listaAux = []
cores = {}
pred = {}


def visita(v):

	cores[v] = "cinza"
	for x in G[v]:
		pred[x] = v
		visita(x)
	cores[v] = "preto"


def main():

	arquivo = open("entrada2.txt","+r")

	linhas = arquivo.read().splitlines()

	A = linhas[0]
	I = linhas[1]

	print("A:",A)
	print("I:",I)

	#gerando lista de adjacencia
	for x in linhas[2:]:
		listaAux = x.split(" ")
		G[listaAux[0]] = listaAux[1:]

	print(G.keys())

	for v in G:
	    cores[v] = "branco"
	    pred[v] = None

	print(cores)

	pilha = [A]

	for v in G:
	    if cores[v] == "branco":
	    	visita(v)

if __name__ == '__main__':
	main()	
