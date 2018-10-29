# -*- coding: utf-8 -*-
import sys

class Graph:
    
    def __init__(self):

        self.data = {}
        self.dist = {}
        self.d = {}
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

        s = aux[0]
              
        data = {}

        for line in aux[1:]:
            v_list     = line.split()
            u          = v_list[0]
            neighbours = v_list[1:]

            #print(u)
            #print(neighbours)

            if data.get(u) == None:
                l = {}
                l[neighbours[0]] = neighbours[1]
                data[u] = l
            else:
                data[u][neighbours[0]] = neighbours[1]  

        self.data = data    
        #print(data)
        return s
    
'''
def getTupleValue(G,u,v):

    for x in G.data[u]:
        if x[0] == v:
            return x[1]
    

def relaxa(G,u,v):
    
    w = getTupleValue(G,u,v)

    if G.d[u] + w < G.d[v]:
       G.d[v] = G.d[u] + w
       G.pred[v] = u
'''

def inicializa(G,s):

    for x in G.data:
        print(x)
        G.dist[x] = float("inf")
        G.pred[x] = -1
    G.d[s] = 0    

def caminhoMinimo(G,s):

    pass

    
G = Graph()
s = G.read("edj.txt",ignore=0)
print(G.data)
print(G.dist)
print(G.pred)

inicializa(G,s)

print(G.data)
print(G.dist)
print(G.pred)