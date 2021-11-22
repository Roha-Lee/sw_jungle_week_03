import collections
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def dfs(at, color):
    global bipartite

    # Not bipartite if existing coloring is differnet from the supposed color
    if node_colors[at] != 0 and node_colors[at] != color:
        bipartite = False
        return

    if visited[at] != 0:
        return

    visited[at] = 1
    node_colors[at] = color

    # Alternative coloring
    if color == 'Blue':
        color = 'Red'
    elif color == 'Red':
        color = 'Blue'

    neighbors = graph[at]

    for next in neighbors:
        dfs(next, color)

for _ in range(int(input())):

    V, E = map(int, input().split())

    graph = collections.defaultdict(list)

    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    bipartite = True
    visited = [0] * (V + 1)
    node_colors = [0] * (V + 1)

    for i in range(1, V + 1):
        if visited[i] == 0:
            dfs(i, 'Blue')

    if bipartite == True:
        print("YES")
    else:
        print('NO')


