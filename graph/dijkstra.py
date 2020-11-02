import sys
from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for col in range(vertices)] for row in range(vertices)]

    def dijkstra(self, s):
        spt = defaultdict(lambda: -1)
        spt_vertices = []

        spt[s] = 0
        spt_vertices = filter(lambda x: x, self.graph[0])

        while len(spt) <= self.vertices:
            min_



if __name__ == '__main__':
    graph = Graph(9)
    g.graph = [
        [0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
    ]
