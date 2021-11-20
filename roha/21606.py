import sys 
from collections import defaultdict
def dfs(graph, node, inout, visited, count=0):
    if inout[node] == 1:
        return count + 1 
    for next_node in graph[node]:
        
        count += dfs(graph, next_node, inout, visited, count)
        inout[next_node] = 1
    return count 

def count_path(n, graph, inout):
    count = 0
    
    for start_node in range(1, n+1):
        if not inout[start_node]:
            visited = [False] * (n+1)
            # visited[start_node] = True
            
            outdoors = dfs(graph, start_node, inout, visited)
            inout[start_node] = 1        
            print(outdoors)
            count += outdoors * (outdoors-1)
    
    return count


if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    inout = list(map(int, '0' + input().rstrip()))
    
    graph = defaultdict(list)
    for _ in range(n-1):
        src, dst = map(int, input().split())
        graph[src].append(dst)
        graph[dst].append(src)
    print(count_path(n, graph, inout))
    

