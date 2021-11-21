from collections import defaultdict
import sys 

# DFS solution
def dfs(graph, node, visited, count = 0):
    for next_node in graph[node]:
        if not visited[next_node]:
            visited[next_node] = True
            count = dfs(graph, next_node, visited, count+1)
    return count 


def find_bids(n, graph):
    half = n // 2
    count = 0
    for bid in range(1, n+1):
        visited = [False] * (n+1)
        visited[bid] = True
        if dfs(graph, bid, visited) > half:
            count += 1
    return count


if __name__ == '__main__':
    input = sys.stdin.readline
    n, m = map(int, input().split())
    forward_graph = defaultdict(list)
    backward_graph = defaultdict(list)
    for _ in range(m):
        heavy, light = map(int, input().split())
        forward_graph[light].append(heavy)
        backward_graph[heavy].append(light)
    print(find_bids(n, forward_graph) + find_bids(n, backward_graph))
