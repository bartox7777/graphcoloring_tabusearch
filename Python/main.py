import random

from MatrixGraph import MatrixGraph
from algorithms import greedy_graph_coloring
from tabusearch import f, tabu_search

def random_coloring(graph, k):
    coloring = []
    for _ in range(k):
        coloring.append(list())
    for node in graph.nodes():
        coloring[random.randint(0, k-1)].append(node)
    return coloring

# graph = MatrixGraph(0, "CPP/mycie14.txt")
graph = MatrixGraph(0, "test_instance.txt")
s = greedy_graph_coloring(graph)
k = len(s)

print(random_coloring(graph, k))
print(graph)

print(tabu_search(graph, k, random_coloring(graph, k), size_of_tabu_list=7, number_of_neighbours=1000, max_number_of_iterations=10000))