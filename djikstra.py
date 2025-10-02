def dijkstra(grafo, inicio):
    visitados = set()
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0

    while len(visitados) < len(grafo):
        # Escogemos el nodo no visitado con menor distancia
        nodo_actual = min((n for n in grafo if n not in visitados),
                          key=lambda n: distancias[n])

        visitados.add(nodo_actual)

        for vecino, peso in grafo[nodo_actual].items():
            nueva_distancia = distancias[nodo_actual] + peso
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia

    return distancias


# Ejemplo de uso
grafo = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2, 'Z': 6},
    'E': {'C': 10, 'D': 2, 'Z': 3},
    'Z': {'D': 6, 'E': 3}
}

print(dijkstra(grafo, 'A'))
