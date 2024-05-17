import pylab as p

def read_graph_as_edges():
    """Считываем граф в виде списка ребер."""
    n = int(input("Количество ребер: "))
    graph = [list(map(int, input(f"ребро {i+1} (начало, конец, вес): ").split())) for i in range(n)]
    return graph

def read_graph_as_neigh_list_w():
    """Считываем граф и преобразуем его в словарь смежности с весами."""
    edge_list = read_graph_as_edges()
    graph_dict = {}
    vertex_set = set()

    for edge in edge_list:
        vertex_set.add(edge[0])
        vertex_set.add(edge[1])

    for v in vertex_set:
        graph_dict[v] = frozenset()

    for edge in edge_list:
        graph_dict[edge[0]] = graph_dict[edge[0]] | frozenset([(edge[1], edge[2])])

    return graph_dict

def Bellman_Ford(graph, start_vertex):
    """Реализуем алгоритм Форда-Беллмана для нахождения кратчайших путей в графе."""
    distance = {vertex: float('inf') for vertex in graph}
    distance[start_vertex] = 0

    for _ in range(len(graph) - 1):
        for vertex in graph:
            for neighbor, weight in graph[vertex]:
                if distance[vertex] != float('inf') and distance[vertex] + weight < distance[neighbor]:
                    distance[neighbor] = distance[vertex] + weight

    for vertex in graph:
        for neighbor, weight in graph[vertex]:
            if distance[vertex] != float('inf') and distance[vertex] + weight < distance[neighbor]:
                print("Граф содержит отрицательный цикл ()\/()")
                return None

    return distance


graph = read_graph_as_neigh_list_w()
result = Bellman_Ford(graph, 1)

if result:
    print("Минимальные расстояния от вершины 1 до остальных вершин:", result)
