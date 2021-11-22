import sys 
from collections import defaultdict, deque

def topological_sort(n, graph):
    result = []
    inward_count = {i:0 for i in range(1, n+1)}
    for node in graph:
        for neighbor in graph[node]:
            inward_count[neighbor] += 1
    q = deque()
    for key, value in inward_count.items():
        if value == 0:
            q.append(key)
    while q:
        node = q.popleft()
        result.append(node)
        for neighbor in graph[node]:
            inward_count[neighbor] -= 1
            if inward_count[neighbor] == 0:
                q.append(neighbor)
    return result
        

if __name__ == '__main__':
    input = sys.stdin.readline
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        src, dst = map(int, input().split())
        graph[src].append(dst)

    print(*topological_sort(n, graph))
