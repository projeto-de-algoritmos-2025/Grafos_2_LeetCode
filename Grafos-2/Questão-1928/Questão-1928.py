import heapq
from collections import defaultdict

class Solution:
    def minCost(self, maxTime, edges, passingFees):
        n = len(passingFees)


        grafo = defaultdict(list)
        for u, v, t in edges:
            grafo[u].append((v, t))
            grafo[v].append((u, t))

        min_tempo = [float('inf')] * n


        fila = [(passingFees[0], 0, 0)]

        while fila:
            custo, tempo, no = heapq.heappop(fila)


            if no == n - 1:
                return custo


            if tempo >= min_tempo[no]:
                continue
            min_tempo[no] = tempo

            for vizinho, tempo_aresta in grafo[no]:
                novo_tempo = tempo + tempo_aresta
                if novo_tempo <= maxTime:
                    novo_custo = custo + passingFees[vizinho]
                    heapq.heappush(fila, (novo_custo, novo_tempo, vizinho))

        return -1
