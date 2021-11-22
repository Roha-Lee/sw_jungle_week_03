import sys 
from collections import defaultdict, deque
# Bellman ford-ish solution Time Complexity O(VE) much slower!
def find_critical_path(n, fgraph, bgraph, start, end):
    distances = {i:-1 for i in range(1, n+1)}
    distances[start] = 0
    q = deque([(start, 0)])
    while q:
        node, dist = q.popleft()
        if dist < distances[node]:
            continue
        for neighbor, cost in fgraph[node]:
            if distances[node] + cost > distances[neighbor]:
                distances[neighbor] = distances[node] + cost
                q.append((neighbor, distances[neighbor]))
    return backtrack_path(n, bgraph, distances, end)

def backtrack_path(n, bgraph, distances, end):
    visited = [False] * (n+1)
    visited[end] = True
    q = deque([end])    
    count = 0
    while q: 
        node = q.popleft()
        for neighbor, cost in bgraph[node]:
            if distances[neighbor] == distances[node] - cost:
                count += 1
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor)
    return distances[end], count

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    
    forward_graph = defaultdict(list)
    backward_graph = defaultdict(list)

    for _ in range(m):
        src, dst, cost = map(int, input().split())
        forward_graph[src].append((dst, cost))
        backward_graph[dst].append((src, cost))
    start, end = map(int, input().split())
    print(*find_critical_path(n, forward_graph, backward_graph, start, end), sep='\n')
    