"""
https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
"""
from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.visited_edges = []

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def traverse(self, s):

        current_node = s

        while len(self.graph) <= len(self.visited_edges):
            if current_node not in self.visited_edges:

                self.visited_edges.append(current_node)






if __name__ == '__main__':
    """
    Input: n = 4, e = 6
    0 -> 1, 0 -> 2, 1 -> 2, 2 -> 0, 2 -> 3, 3 -> 3
    """
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(3, 3)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)


    graph.traverse()