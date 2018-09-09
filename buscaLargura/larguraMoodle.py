# -*- coding: utf-8 -*-
import sys

class Graph:
    
    def __init__(self):

        self.data = {}
        self.dist = {}
        self.cores = {}
        self.fila = []
        self.pred = {}

    def read(self,filename=None,ignore=0):
        
        if filename:
           f = open(filename)
        else:   
           f = sys.stdin
        
        while ignore>0: # ignora linhas iniciais do problema para ler somente o grafo
            f.readline()
            ignore -= 1
        
        data = {}
        for line in f:
            v_list     = line.split()
            u          = v_list[0]
            neighbours = v_list[1:] 
            data[u]       = neighbours
            #print(data)
        
        self.data = data    
        
        return data
    
    def add_edge(self,u,v): # para fazer em memória
        
        try:
            self.data[u].append(v)
        except:
            self.data[u] = [v]
        
    def add_neighbours(self,u,n_list):
        
        try:
            self.data[u] += n_list
        except:
            self.data[u] = n_list
    
    def check(self): # garante que não hajam vértices repetidos

        data = self.data
        for v in data:
            data[v] = list(set(data[v]))

    def __str__(self):

        s = "############# Graph ###############\n"
        s+= str(self.data)
        s+= "###################################\n"        
        return s

def largura(G,s):

    for x in G.data:
        if x != s:
            G.dist[x] = 0
            G.cores[x] = "branca"

    G.dist[s] = 0
    G.cores[s] = "azul"
    G.pred[s] = None
    G.fila.append(s)

    while len(G.fila) > 0:

        u = G.fila[0]

        for v in G.data[u]:
            if G.cores[v] == "branca": # vertice nunca foi visitado
                G.cores[v] = "azul"
                G.dist[v] = G.dist[u] + 1
                G.pred[v] = u # seta predecessor de um vertice
                G.fila.append(v)
        
        
        
        G.fila.pop(0) 
        G.cores[u] = "azul"
    
    # ordenando dic
    G.dist = sorted(G.dist.items(), key=lambda t:t[0])
    
    for k,v in G.dist:
        if k != s:
	        print(s+" "+str(k)+" "+str(v))
    
G = Graph()
G.read(filename=None,ignore=1)
largura(G,"A")

