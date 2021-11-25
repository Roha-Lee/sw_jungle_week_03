import sys 
sys.setrecursionlimit(100000000)

class DisjointSet:
    def __init__(self, max_node):
        self.parent = {i:i for i in range(1, max_node+1)}
        self.rank = {i:0 for i in range(1, max_node+1)}
        
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
                self.rank[y] += 1
            else:
                self.parent[y] = x
                self.rank[y] = self.rank[x]
        
def get_mst_costs(edges, n):
    ds = DisjointSet(n)
    edges = sorted(edges)
    mst_cost = 0
    for cost, src, dst in edges:
        if ds.find(src) != ds.find(dst):
            mst_cost += cost
            ds.union(src, dst)
    return mst_cost

if __name__ == '__main__':
    input = sys.stdin.readline
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        src, dst, cost = map(int, input().split())
        edges.append((cost, src, dst))
    print(get_mst_costs(edges, n))
    

