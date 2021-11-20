import sys 
from collections import defaultdict

class DisjointSet:
    def __init__(self, max_val):
        self.parent = {i:i for i in range(1, max_val+1)} 
        self.rank = {i:0 for i in range(1, max_val+1)}
        self.cc = max_val

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
            self.cc -= 1

    def get_component_nums(self):
        isolated = sum([val == 0 for val in self.rank.values()])
        return self.cc, isolated

        
def is_bipartite_graph(graph, v, start, isolated):
    ds = DisjointSet(v)
    for node in graph:
        neighbors = graph[node]
        if neighbors:
            first = neighbors[0]
            for second in neighbors:
                ds.union(first, second)
    
    end, _ = ds.get_component_nums()
    const = (end - isolated) / (start - isolated)
    
    if const == float(2):
        return "YES"
    else:
        return "NO"

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
        start, isolated = ds.get_component_nums()
        print(is_bipartite_graph(graph, v, start, isolated))

