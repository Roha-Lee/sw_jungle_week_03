import collections
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = collections.defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (n + 1)
count = 0

def count_components():
    global count
    for node in range(1, n + 1):
        if visited[node] == 0:
            count += 1
            dfs(node)
    return count

def dfs(at):
    if visited[at] != 0:
        return

    visited[at] = 1

    neighbors = graph[at]

    for next in neighbors:
        dfs(next)

print(count_components())