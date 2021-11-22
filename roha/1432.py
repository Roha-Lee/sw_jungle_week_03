import sys 
from collections import  defaultdict
from heapq import heappush, heappop
def fix_graph(n, graph):
    result = []
    q = []
    inwards_count = {i:0 for i in range(n)}
    for key in graph:
        for neighbor in graph[key]:
            inwards_count[neighbor] += 1
    for key, value in inwards_count.items():
        if value == 0:
            heappush(q, -key)
    while q:
        node = -heappop(q)
        # 0-index -> 1-index
        result.append(node + 1)
        for neighbor in graph[node]:
            inwards_count[neighbor] -= 1
            if inwards_count[neighbor] == 0:
                heappush(q, -neighbor)
    
    result.reverse()
    if len(result) == n:
        result, index = zip(*sorted(zip(result, range(1, n+1))))
        return index
    return [-1]

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    adjacent_matrix = []
    for _ in range(n):
        adjacent_matrix.append(list(map(int, input().rstrip())))
    graph = defaultdict(list)
    
    for src in range(n):
        for dst in range(n):
            if adjacent_matrix[src][dst]:
                graph[dst].append(src)
    
    print(*fix_graph(n, graph))
    