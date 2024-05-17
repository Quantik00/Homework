def read_graph_as_edges():
    """Считываем граф в виде списка ребер с вершинами и весами как строки."""
    n = int(input("количество ребер: "))
    graph = [list(map(str, input(f"ребро {i+1} (начало, конец, вес): ").split())) for i in range(n)]
    return graph

def read_graph_as_neigh_list_w():
    "Считываем граф и преобразуем его в словарь смежности с весами."
    edge_list = read_graph_as_edges()
    graph_dict = {}
    vertex_set = set()

    for edge in edge_list:
        vertex_set.add(int(edge[0]))
        vertex_set.add(int(edge[1]))

    for v in vertex_set:
        graph_dict[v] = frozenset()

    for edge in edge_list:
        graph_dict[int(edge[0])] = graph_dict[int(edge[0])] | frozenset([(int(edge[1]), edge[2])])

    return graph_dict

def read_graph_as_neigh_matrix():
    "Считываем граф и преобразуем его в матрицу смежности."
    edge_list = read_graph_as_edges()
    vertex_set = set()

    for edge in edge_list:
        vertex_set.add(edge[0])
        vertex_set.add(edge[1])

    V_num = len(vertex_set)
    res_matrix = [[0 for _ in range(V_num)] for _ in range(V_num)]

    for edge in edge_list:
        index_1 = int(edge[0]) - 1
        index_2 = int(edge[1]) - 1
        res_matrix[index_1][index_2] = edge[1]

    return res_matrix

def read_graph_as_neigh_matrix_w():
    "Считываем граф и преобразуем его в взвешенную матрицу смежности."
    edge_list = read_graph_as_edges()
    vertex_set = set()

    for edge in edge_list:
        vertex_set.add(edge[0])
        vertex_set.add(edge[1])

    V_num = len(vertex_set)
    res_matrix = [[0 for _ in range(V_num)] for _ in range(V_num)]

    for edge in edge_list:
        index_1 = int(edge[0]) - 1
        index_2 = int(edge[1]) - 1
        res_matrix[index_1][index_2] = edge[2]

    return res_matrix

def print_matrix(matrix):
    for line in matrix:
        print(*line)

def Dijkstra(graph, start_vertex):
    "Реализуем Дейкстра для нахождения кратчайших путей в графе."
    d = {key: 'lololo' for key in graph.keys()}
    visited = []
    end = []

    d[start_vertex] = ''
    visited.append([0, start_vertex])

    while visited:
        visited.sort()
        current = visited.pop(0)
        current_vertex = current[1]
        end.append(current_vertex)

        for neigh in graph[current_vertex]:
            neighbor, weight = neigh
            if neighbor not in end:
                if d[neighbor] == 'lololo':
                    d[neighbor] = d[current_vertex] + weight
                    visited.append([weight, neighbor])
                elif d[current_vertex] + weight < d[neighbor]:
                    d[neighbor] = d[current_vertex] + weight
                    visited.append([weight, neighbor])

    return d

graph = read_graph_as_neigh_list_w()
shortest_paths = Dijkstra(graph, 1)
print("Граф в виде словаря смежности с весами:", graph)
print("Кратчайшие пути от вершины 1:", shortest_paths)

