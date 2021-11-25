import sys 
# Floyd warshal algorithm
def find_bids(n, graph):
    half = n // 2
    src = 1
    for inter in range(1, n+1):
        for src in range(1, n+1):
            for dst in range(1, n+1):
                graph[src][dst] = min(graph[src][dst], graph[src][inter] + graph[inter][dst])
    count = 0
    for i in range(1, n+1):
        if half < len(list(filter(lambda x: 1 <= x < float('inf'), graph[i]))):
            count += 1
    return count 

if __name__ == '__main__':
    input = sys.stdin.readline
    n, m = map(int, input().split())
    forward_graph = [[0 if i==j else float('inf') for j in range(n+1)] for i in range(n+1)]
    backward_graph = [[0 if i==j else float('inf') for j in range(n+1)] for i in range(n+1)]
    for _ in range(m):
        heavy, light = map(int, input().split())
        forward_graph[light][heavy] = 1
        backward_graph[heavy][light] = 1
    print(find_bids(n, forward_graph) + find_bids(n, backward_graph))