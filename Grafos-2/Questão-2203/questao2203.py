import heapq
from collections import defaultdict

class Solution(object):
    def dijkstra(self, n, grafo, inicio):
        """
        Executa o algoritmo de Dijkstra para encontrar as menores distâncias
        a partir do nó 'inicio' até todos os outros nós do grafo.
        """
        dist = [float('inf')] * n
        dist[inicio] = 0
        heap = [(0, inicio)]

        while heap:
            custo_atual, u = heapq.heappop(heap)
            if custo_atual > dist[u]:
                continue
            for vizinho, peso in grafo[u]:
                if dist[vizinho] > custo_atual + peso:
                    dist[vizinho] = custo_atual + peso
                    heapq.heappush(heap, (dist[vizinho], vizinho))
        return dist

    def minimumWeight(self, n, arestas, src1, src2, destino):
        """
        Encontra o menor peso de um subgrafo onde tanto src1 quanto src2
        conseguem alcançar o nó 'destino'.
        """
        # Construímos o grafo direto e o grafo reverso
        grafo = defaultdict(list)
        grafo_reverso = defaultdict(list)

        for u, v, peso in arestas:
            grafo[u].append((v, peso))
            grafo_reverso[v].append((u, peso))  # Reverso usado para voltar do destino

        # Calculamos as distâncias de src1, src2 e destino (no grafo reverso)
        dist1 = self.dijkstra(n, grafo, src1)
        dist2 = self.dijkstra(n, grafo, src2)
        dist3 = self.dijkstra(n, grafo_reverso, destino)  # equivale a v → destino

        menor_custo = float('inf')

        # Verificamos todos os nós como possíveis "encontros" dos caminhos
        for v in range(n):
            if dist1[v] < float('inf') and dist2[v] < float('inf') and dist3[v] < float('inf'):
                custo_total = dist1[v] + dist2[v] + dist3[v]
                menor_custo = min(menor_custo, custo_total)

        return menor_custo if menor_custo < float('inf') else -1


# -----------------------------
# 🔽 Modo de entrada interativo
# -----------------------------
if __name__ == "__main__":
    # Exemplo de entrada:
    # 6
    # [[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]]
    # 0
    # 1
    # 5

    import ast

    print("Digite o número de nós:")
    n = int(input())

    print("Digite a lista de arestas no formato [[u,v,peso], ...]:")
    arestas = ast.literal_eval(input())

    print("Digite o nó de origem src1:")
    src1 = int(input())

    print("Digite o nó de origem src2:")
    src2 = int(input())

    print("Digite o nó de destino:")
    destino = int(input())

    solucao = Solution()
    resultado = solucao.minimumWeight(n, arestas, src1, src2, destino)
    
    print("Menor peso do subgrafo:", resultado)
