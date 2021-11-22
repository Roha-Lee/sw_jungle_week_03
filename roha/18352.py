import sys 
from collections import defaultdict
from heapq import heappush, heappop

def find_loc_from_x_with_dist_k(n, graph, x, k):
    dists = {i:float('inf') for i in range(1, n+1)}
    dists[x] = 0
    q = [(0, x)]
    while q:
        d, loc = heappop(q)
        if dists[loc] < d:
            continue
        for neighbor in graph[loc]:
            if dists[neighbor] > d + 1:
                dists[neighbor] = d + 1
                heappush(q, (dists[neighbor], neighbor))
    result = []
    for key, val in dists.items():
        if val == k:
            result.append(key)
    return result
    

if __name__ == '__main__':
    input = sys.stdin.readline
    n, m, k, x = map(int, input().split())
    
    graph = defaultdict(list)
    for _ in range(m):
        src, dst = map(int, input().split())
        graph[src].append(dst)
    result = find_loc_from_x_with_dist_k(n, graph, x, k)
    if result:
        print(*sorted(result), sep='\n')
    else:
        print(-1)
