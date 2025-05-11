import heapq

class Solution:
    def minCostConnectPoints(self, pontos):
        n = len(pontos)
        visitado = [False] * n
        fila_prioridade = [(0, 0)]
        custo_total = 0
        arestas_utilizadas = 0

        while arestas_utilizadas < n:
            custo, u = heapq.heappop(fila_prioridade)

            if visitado[u]:
                continue

            visitado[u] = True
            custo_total += custo
            arestas_utilizadas += 1

            for v in range(n):
                if not visitado[v]:
                    distancia = abs(pontos[u][0] - pontos[v][0]) + abs(pontos[u][1] - pontos[v][1])
                    heapq.heappush(fila_prioridade, (distancia, v))

        return custo_total
