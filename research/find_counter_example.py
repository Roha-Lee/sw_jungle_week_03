from sys import stdin, setrecursionlimit
from collections import deque
setrecursionlimit(10**9)

#정점의 개수 N, 간선의 개수 M, 정점의 번호 V
N, M, V = [int(x) for x in stdin.readline().split()]

edge = {}
for _ in range(M):
    a, b =[int(x) for x in stdin.readline().split()]
    try:
        edge[a].append(b)
    except:
        edge[a] = [b]
    try:
        edge[b].append(a)
    except:
        edge[b] = [a]

for key in edge:
    edge[key] = list(set(edge[key]))
    edge[key].sort()


dfs_visit = []
bfs_visit = []
def DFS(root):
    if len(dfs_visit) == N:
        return
    
    dfs_visit.append(root)
    for i in range(len(edge[root])):
        if edge[root][i] not in dfs_visit:
            DFS(edge[root][i])

    return

def BFS(root):
    q = deque()
    q.append(root)
    while q and len(bfs_visit)<N:
        root = q.popleft()
        bfs_visit.append(root)
        for i in range(len(edge[root])):
            if edge[root][i] not in bfs_visit:
                q.append(edge[root][i])


if V in edge:
    DFS(V)
    print(" ".join(map(str,dfs_visit)))
    BFS(V)
    print(" ".join(map(str,bfs_visit)))
else:
    print(V)
    print(V)