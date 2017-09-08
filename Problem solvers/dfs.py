class Graph:
    def __init__(self, values, adjacency_list):
        self.values = values
        self.adjacency_list = adjacency_list


def DFS(g, vertex, discovered={}):
    # type/null checks

    if vertex not in discovered:
        discovered[vertex] = True

        for i in g.adjacency_list[vertex]:
            discovered.update(DFS(g, i, discovered))

    return discovered


if __name__ == '__main__':
    values = [1, 1, 1, 1, 1, 1, 1]
    adjacency_list = [
        [1, 2],
        [2, 4, 5],
        [1],
        [3, 1],
        [0],
        [4],
        [5]
    ]
    graph = Graph(values, adjacency_list)

    print(DFS(graph, 0))

