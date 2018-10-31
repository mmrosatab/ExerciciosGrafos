# -*- coding: utf-8 -*-
import sys

class Graph:
    
    def __init__(self):

        self.data = {}
        self.d = {}
        self.fila = {}
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
                #data[neighbours[0]] = {} 
                data[neighbours[0]] = {u: int(neighbours[1])}
            else:
                data[neighbours[0]][u] = int(neighbours[1])

        self.data = data    
        #print(data)
        return aux[0]
    
def relaxa(G,u,v):

    w = G.data[u][v]

    if G.d[u] + w < G.d[v]:
        G.d[v] = G.d[u] + w
        G.pred[v] = u


def inicializa(G,s):

    for x in G.data:

        G.d[x] = G.fila[x] = float("inf")
        G.pred[x] = -1
    
    G.d[s] = 0 
    G.fila[s] = 0 
    G.pred[s] = 'NULL' 
     

def dijkstra(G,s):

    inicializa(G,s)

    while len(G.fila) > 0:
        
        u = min(G.fila, key=G.fila.get)

        for k,v in G.data[u].iteritems():
            relaxa(G,u,k)
        del G.fila[u]

G = Graph()
s = G.read("edj.txt",ignore=0)

dijkstra(G,s)

pred = sorted(G.pred.items(), key=lambda t:t[0])
    
for k,v in pred:
    print(k+" "+v)
