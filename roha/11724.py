import sys 
sys.setrecursionlimit(100000000)

class DisjointSet:
    def __init__(self, max_node):
        self.parent = {i:i for i in range(1, max_node+1)}
        self.rank = {i:0 for i in range(1, max_node+1)}
        self.cc = max_node
    
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
                self.parent[y] = x
                self.rank[x] += 1
            else:
                self.parent[y] = x
                self.rank[y] = self.rank[x]
            self.cc -= 1
        
    def get_connected_component_num(self):
        return self.cc

if __name__ == '__main__':
    input = sys.stdin.readline
    n, m = map(int, input().split())
    edges = []
    ds = DisjointSet(n)
    for _ in range(m):
        src, dst = map(int, input().split())
        ds.union(src, dst)
    print(ds.get_connected_component_num())