import sys 
from collections import defaultdict
from collections import deque

def dfs(graph, root, visited, result):
    for next_node in graph[root]:
        if not visited[next_node]:
            result.append(next_node)
            visited[next_node] = True
            dfs(graph, next_node, visited, result)
    return result

def bfs(graph, root, visited, result):
    q = deque([root])
    while q:
        curr = q.popleft()
        if visited[curr]:
            continue
        
        result.append(curr)
        visited[curr] = True
        for next_node in graph[curr]:
            if not visited[next_node]:
                
                q.append(next_node)    
    return result
    

if __name__ == '__main__':
    input = sys.stdin.readline
    graph = defaultdict(list)
    n, m, v = map(int, input().split())
    for _ in range(m):
        src, dst = map(int, input().split())
        graph[src].append(dst)
        graph[dst].append(src)
    
    for key in graph:
        graph[key] = sorted(graph[key])
    
    visited = [False] * (n + 1)
    visited[v] = True
    print(*dfs(graph, v, visited, [v]))
    visited = [False] * (n + 1)
    print(*bfs(graph, v, visited, []))
    
