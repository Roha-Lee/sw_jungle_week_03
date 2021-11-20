# 4	1260	하	그래프 탐색 기본	DFS와 BFS	9-1
'''
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000),
탐색을 시작할 정점의 번호 V가 주어진다. 
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다.
입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다.
V부터 방문된 점을 순서대로 출력하면 된다.

반례:
4 6 1
1 2
1 2
1 3
1 4
2 4
3 4

#BFS 75번째 줄 + and edge[root][i] not in q 해결
'''
from sys import stdin, setrecursionlimit, version_info
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
        if root not in bfs_visit: 
            bfs_visit.append(root)
        for i in range(len(edge[root])):
            if edge[root][i] not in bfs_visit and edge[root][i] not in q:
                q.append(edge[root][i])


if V in edge:
    DFS(V)
    print(*dfs_visit)
    BFS(V)
    print(*bfs_visit)
else:
    print(V)
    print(V)
