import queue

class Graph:
    def __init__(self, values, adjacency_list):
        self.values = values
        self.adjacency_list = adjacency_list

def BFS(g, vertex, q = None):
    q = queue.Queue() if q is None else q
    q.put(vertex)
    discovered = []
    print("q is: ", q)
    while not q.empty():
        current = q.get()
        print("current is: ", current)
        if current not in discovered:
            discovered.append(current)
            for n in g.adjacency_list[current]:
                q.put(n)

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

    print(BFS(graph, 0))



