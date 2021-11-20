import sys 
from collections import defaultdict

def dfs(graph, node, inout, count=0):
    if inout[node] == 2:
        return count 
    if inout[node] == 1:
        return count + 1 
    
    inout[node] = 2
    for next_node in graph[node]:
        if inout[next_node] == 2:
            continue
        count = dfs(graph, next_node, inout, count)
    return count 

def count_path(n, graph, inout):
    count = 0
    for start_node in range(1, n+1):
        if inout[start_node] == 0:
            outdoors = dfs(graph, start_node, inout)     
            count += outdoors * (outdoors-1)
    for start_node in range(1, n+1):
        if inout[start_node] == 1:
            inout[start_node] = 0
            outdoors = dfs(graph, start_node, inout) 
            inout[start_node] = 1    
            count += outdoors
    return count


if __name__ == '__main__':
    sys.setrecursionlimit(100000000)
    input = sys.stdin.readline
    n = int(input())
    inout = list(map(int, '0' + input().rstrip()))
    
    graph = defaultdict(list)
    for _ in range(n-1):
        src, dst = map(int, input().split())
        graph[src].append(dst)
        graph[dst].append(src)
    print(count_path(n, graph, inout))
    

