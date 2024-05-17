def read_graph_as_edges():
    n = int(input("Введите количество ребер: "))
    graph = [list(map(int, input(f"Введите ребро {i+1}: ").split())) for i in range(n)]
    return graph

def read_graph_as_neigh_list_w():
    print("На вход сначала подается одно число (q) - количество ребер. \n"
          "Потом в каждой новой строке необходимо вводить 5 чисел: \n"
          "1-е - вершина, начало ребра \n"
          "2-е - ее цвет (цвета обозначаются цифрами: различные цвета различными цифрами) \n"
          "3-е - вершина, конец ребра \n"
          "4-е - её цвет \n"
          "5-е - вес ребра")
    edge_list = read_graph_as_edges()
    graph_dict = {}
    vertex_set = set()
    for edge in edge_list:
        vertex_set.add(edge[0])
        vertex_set.add(edge[2])
    for v in vertex_set:
        graph_dict[v] = frozenset()
    for edge in edge_list:
        graph_dict[edge[0]] = graph_dict[edge[0]] | frozenset([(edge[1], edge[2], edge[3], edge[4])])
    return graph_dict

def Dijkstra(graph, start_vertex):
    d = {key: float('infinity') for key in graph.keys()}
    colors = {key: float('infinity') for key in graph.keys()}
    visited = []
    finished = []
    
    d[start_vertex] = 0
    colors[start_vertex] = 0
    visited.append([0, 0, start_vertex])  # [change of color, weight, vertex]
    
    while visited:
        visited.sort()
        current = visited.pop(0)
        current_vertex = current[2]
        finished.append(current_vertex)
        
        for neigh in graph[current_vertex]:
            if neigh[1] not in finished:
                if list(graph[current_vertex])[0][0] == neigh[2]:
                    colors[neigh[1]] = colors[current_vertex]
                    if d[current_vertex] + neigh[3] < d[neigh[1]]:
                        d[neigh[1]] = d[current_vertex] + neigh[3]
                    visited.append([colors[neigh[1]], neigh[3], neigh[1]])
                else:
                    if colors[neigh[1]] == float('inf'):
                        colors[neigh[1]] = colors[current_vertex] + 1
                        if d[current_vertex] + neigh[3] < d[neigh[1]]:
                            d[neigh[1]] = d[current_vertex] + neigh[3]
                    if colors[neigh[1]] > colors[current_vertex]:
                        visited.append([colors[neigh[1]], neigh[3], neigh[1]])
    
    return d, colors

graph = read_graph_as_neigh_list_w()
print("Граф в виде словаря смежности:", graph)
print("Соседи вершины 1:", graph[1])

d, c = Dijkstra(graph, 1)
print("Минимальные расстояния от вершины 1 до остальных:", d)
print("Количество смен цвета при достижении каждой вершины:", c)
