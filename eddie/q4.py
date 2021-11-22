import collections
import sys
from collections import deque
input = sys.stdin.readline

n, m, start_node = map(int, input().split())

graph = collections.defaultdict(list) # allows use of append in graph
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[u].sort()
    graph[v].append(u)
    graph[v].sort()

visited = [0] * (n + 1)
dfs_path = []

def dfs(at):
    if visited[at] != 0:
        return

    dfs_path.append(at)
    visited[at] = 1

    neighbors = graph[at]

    for next in neighbors:
        dfs(next)

dfs(start_node)
print(*dfs_path)


visited = [0] * (n + 1)
bfs_path = []
queue = deque()

def bfs(node):
    queue.append(node)
    visited[node] = 1

    while queue:
        node = queue.popleft()
        bfs_path.append(node)
        neighbors = graph[node]

        for next in neighbors:
            if visited[next] == 0:
                queue.append(next)
                visited[next] = 1

bfs(start_node)
print(*bfs_path)

