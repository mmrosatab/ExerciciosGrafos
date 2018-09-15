# -*- coding: utf-8 -*-
import sys
pilha = []

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
        
        aux = f.read().splitlines()

        s = aux[0]
        i = aux[1]
              
        data = {}
        for line in aux[2:]:
            v_list     = line.split()
            u          = v_list[0]
            neighbours = v_list[1:] 
            data[u]       = neighbours
            #print(data)
        
        self.data = data    
        #print(data)
        return s,i
    
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

def visita(G,u,a,i):

    G.cores[u] = "cinza"
    pilha.append(u)
    #print(pilha)

    for x in G.data[u]:
        if G.cores[x] == "branco":
            visita(G,x,a,i)

            if pilha[0] == a and pilha[-1] == i:

                caminho = ' '.join([i for i in pilha])
                print(caminho)

            pilha.pop()
    
        
def profundidade(G,a,i):

    #print("datainhança atual",G.data)
    for x in G.data:
        if G.cores[x] == "branco":
            visita(G,x,a,i)

    
G = Graph()
s,i = G.read("entrada2.txt",ignore=0)

for v in G.data.keys():
    G.cores[v] = "branco"
#G.read(filename=None,ignore=2)
profundidade(G,s,i)