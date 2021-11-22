import sys 
from collections import defaultdict
from heapq import heappush, heappop

def find_min_cost(n, graph, start, end):
    dists = {i:float('inf') for i in range(1, n+1)}
    dists[start] = 0
    q = [(0, start)]
    while q:
        d, loc = heappop(q)
        if dists[loc] < d:
            continue
        for cost, neighbor in graph[loc]:
            if dists[neighbor] > d + cost:
                dists[neighbor] = d + cost
                heappush(q, (dists[neighbor], neighbor))
    return dists[end]

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    graph = defaultdict(list)
    for _ in range(m):
        src, dst, cost = map(int, input().split())
        graph[src].append((cost, dst))
    start, end = map(int, input().split())
    print(find_min_cost(n, graph, start, end))
    