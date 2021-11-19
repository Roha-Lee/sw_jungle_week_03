import sys 
from collections import defaultdict, Counter

class DisjointSet:
    def __init__(self, max_val):
        self.parent = {i:i for i in range(1, max_val+1)} 
        self.rank = {i:0 for i in range(1, max_val+1)}
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y: 
            if self.rank[x] < self.rank[y]:
                self.parent[x] = y
                self.rank[x] = self.rank[y]
            elif self.rank[x] == self.rank[y]:
                self.parent[x] = y
                self.rank[x] += 1
                self.rank[y] += 1
            else:
                self.parent[y] = x
                self.rank[y] = self.rank[x]


def get_component_from_ds(ds):
    cntr = Counter(ds.parent.values())
    count = sum([value > 1 for value in cntr.values()])
    return count
        
        
def is_bipartite_graph(graph, v, graph_components):
    ds = DisjointSet(v)
    for node in graph:
        neighbors = graph[node]
        if neighbors:
            first = neighbors[0]
            for second in neighbors:
                ds.union(first, second)
    
    calc_components = get_component_from_ds(ds)
    print(calc_components, graph_components)
    # if cl

if __name__ == '__main__':
    input = sys.stdin.readline
    testcase = int(input())
    for _ in range(testcase):
        v, e = map(int, input().split())
        graph = defaultdict(list)
        ds = DisjointSet(v)
        for _ in range(e):
            src, dst = map(int, input().split())
            graph[src].append(dst)
            graph[dst].append(src)
            ds.union(src, dst)
        components = get_component_from_ds(ds)
        print(is_bipartite_graph(graph, v, components))

