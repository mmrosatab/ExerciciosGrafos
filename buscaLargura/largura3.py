# -*- coding: utf-8 -*-
import sys

class Grafo():

    def __init__(self):
        self.viz = {}
        self.dist = {}
        self.cores = {}
        self.fila = []
        self.pred = {}
        
def largura(G,s):

    for x in G.viz:
        if x != s:
            G.dist[x] = 0
            G.cores[x] = "branca"

    G.dist[s] = 0
    G.cores[s] = "azul"
    G.pred[s] = None
    G.fila.append(s)

    while len(G.fila) > 0:

        u = G.fila[0]

        for v in G.viz[u]:
            if G.cores[v] == "branca": # vertice nunca foi visitado
                G.cores[v] = "azul"
                G.dist[v] = G.dist[u] + 1
                G.pred[v] = u # seta predecessor de um vertice
                G.fila.append(v)
        
        
        
        G.fila.pop(0) #tira o primeiro vertice da fila

        G.cores[u] = "azul"

    # ordenando dic
    G.dist = sorted(G.dist.items(), key=lambda t:t[0])
    
    for k,v in G.dist:
        if k != s:
            print(s+" "+str(k)+" "+str(v))
    

def main():

    
    listaAux = []
    arquivo = open("entrada.txt","r")
    linhas = arquivo.read().splitlines()

    G = Grafo()
    #gerando lista de adjacencia
    for x in linhas:
        listaAux = x.split(" ")
        G.viz[listaAux[0]] = listaAux[1:] 
    
    largura(G,"A")

    #print(dist)
    
if __name__ == '__main__':
    main()
