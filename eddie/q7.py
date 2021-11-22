import collections
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

N = int(input())
visited = [0] * (N + 1)

graph = collections.defaultdict(list)

for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

parents = {}

def dfs(at):
    if visited[at] != 0:
        return

    visited[at] = 1
    nexts = graph[at]

    for next in nexts:
        if visited[next] == 0:
            parents[next] = at
        dfs(next)

dfs(1)

for i in range(2, N + 1):
    print(parents[i])
