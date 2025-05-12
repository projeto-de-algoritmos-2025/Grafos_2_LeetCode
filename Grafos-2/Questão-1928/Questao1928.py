import heapq
from collections import defaultdict

def menor_custo(max_time, arestas, taxas_passagem):
    n = len(taxas_passagem)

    # Monta o grafo com lista de adjacência
    grafo = defaultdict(list)
    for u, v, tempo in arestas:
        grafo[u].append((v, tempo))
        grafo[v].append((u, tempo))  # Porque o grafo é bidirecional

    # Fila de prioridade com: (custo acumulado, tempo acumulado, cidade atual)
    fila = [(taxas_passagem[0], 0, 0)]

    # visited[cidade][tempo] = menor custo para chegar à cidade com tempo específico
    visitado = [[float('inf')] * (max_time + 1) for _ in range(n)]
    visitado[0][0] = taxas_passagem[0]

    while fila:
        custo, tempo, cidade = heapq.heappop(fila)

        if cidade == n - 1:
            return custo

        for vizinho, t in grafo[cidade]:
            tempo_total = tempo + t
            if tempo_total > max_time:
                continue

            custo_total = custo + taxas_passagem[vizinho]

            if visitado[vizinho][tempo_total] > custo_total:
                visitado[vizinho][tempo_total] = custo_total
                heapq.heappush(fila, (custo_total, tempo_total, vizinho))

    return -1


# ======== Entrada e teste pelo terminal ===========
if __name__ == "__main__":
    print("Digite o tempo máximo permitido:")
    maxTime = int(input())

    print("Digite a lista de arestas no formato [u, v, tempo], uma por linha. Digite 'fim' para encerrar:")
    edges = []
    while True:
        linha = input()
        if linha.lower() == 'fim':
            break
        edges.append(list(map(int, linha.strip('[]').split(','))))

    print("Digite as taxas de passagem para cada cidade separadas por espaço:")
    passingFees = list(map(int, input().split()))

    resultado = menor_custo(maxTime, edges, passingFees)
    print("\nMenor custo possível:", resultado)
