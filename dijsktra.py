# -*- coding: utf-8 -*-
import sys

class Graph:
    
    def __init__(self):

        self.data = {}
        self.dist = {}
        self.pred = {}

    def read(self,filename=None,ignore=0):
        
        if filename:
           f = open(filename)
        else:   
           f = sys.stdin
        
        while ignore>0: # ignora linhas iniciais do problema para ler somente o grafo
            f.readline()
            ignore -= 1
        
        aux = f.read().splitlines()
  
        data = {}

        for line in aux[1:]:
            v_list     = line.split()
            u          = v_list[0]
            neighbours = v_list[1:]

            #print(u)
            #print(neighbours)

            if data.get(u) == None:

                l = {}
                l[neighbours[0]] = int(neighbours[1])
                data[u] = l
            else:
                data[u][neighbours[0]] = int(neighbours[1])  

            if data.get(neighbours[0]) == None: # caso um dos vizinhos nao exista aresta incidindo em outro vertice
                #print("Entrei")
                #print(neighbours[0])
                data[neighbours[0]] = {} 

        self.data = data    
        #print(data)
        return aux[0]
    

def pesoAresta(G,u,v):

    for x,y in G.data[u].iteritems():
        if x == v:
            return y
   

def relaxa(G,u,v):
    

    w = pesoAresta(G,u,v)
    
    #print(G.dist[u])
    #print(G.dist[v])

    if G.dist[u] + w < G.dist[v]:
       G.dist[v] = G.dist[u] + w
       G.pred[v] = u


def inicializa(G,s):

    for x in G.data:
        
        #print("data:",x)

        G.dist[x] = 1000
        G.pred[x] = -1
    
    G.dist[s] = 0    


def caminhoMinimo(G,s):

    G.dist = dict(sorted(G.dist.items(), key=lambda t:t[1]))
    #print("Estado Distancias: ", G.dist)

    while len(G.dist) > 0:

        # minimo da fila
        u = min(G.dist, key=G.dist.get)
        

        for k,v in G.data[u].iteritems():

            relaxa(G,u,k)

        del G.dist[u]

        G.dist = dict(sorted(G.dist.items(), key=lambda t:t[1]))
        #print("Estado Distancias: ", G.dist)


G = Graph()
s = G.read("edj.txt",ignore=0)

print(s)
print(G.data)

inicializa(G,s)

print("Distancias:", G.dist)
print("Predecessores: ", G.pred)

caminhoMinimo(G,s)

#print("Distancias:", G.dist)
#print("Predecessores: ", G.pred)
