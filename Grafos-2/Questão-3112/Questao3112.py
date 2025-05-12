import heapq

def menor_tempo_para_alcancar_nos(n, arestas, desaparecer):
    grafo = [[] for _ in range(n)]
    for u, v, tempo in arestas:
        grafo[u].append((v, tempo))
        grafo[v].append((u, tempo))

    distancia = [float('inf')] * n
    distancia[0] = 0

    fila = [(0, 0)]

    while fila:
        tempo_atual, no_atual = heapq.heappop(fila)

        if tempo_atual > distancia[no_atual]:
            continue

        for vizinho, custo in grafo[no_atual]:
            novo_tempo = tempo_atual + custo
            if novo_tempo < desaparecer[vizinho] and novo_tempo < distancia[vizinho]:
                distancia[vizinho] = novo_tempo
                heapq.heappush(fila, (novo_tempo, vizinho))

    resposta = []
    for i in range(n):
        if distancia[i] == float('inf') or distancia[i] >= desaparecer[i]:
            resposta.append(-1)
        else:
            resposta.append(distancia[i])

    return resposta


# -----------------------------
# 🔽 Modo de entrada interativo
# -----------------------------
if __name__ == "__main__":
    print("Digite o número de nós:")
    n = int(input())

    print("Digite o número de arestas:")
    m = int(input())

    arestas = []
    print("Digite as arestas no formato: u v tempo")
    for _ in range(m):
        u, v, t = map(int, input().split())
        arestas.append((u, v, t))

    print("Digite os tempos de desaparecimento dos nós (separados por espaço):")
    desaparecer = list(map(int, input().split()))

    resultado = menor_tempo_para_alcancar_nos(n, arestas, desaparecer)
    print("Saída:")
    print(" ".join(map(str, resultado)))
