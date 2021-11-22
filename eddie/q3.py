import heapq
import collections
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [0] * (n + 1) # add 1 since node numbering starts from 1

graph = collections.defaultdict(list) # create empty dictionary to store undirected edge data

for i in range(m): # populate undirected edge data
    u, v, weight = map(int, input().split())
    graph[u].append([weight, u, v])
    graph[v].append([weight, v, u])

def prim(graph, start_node):
    visited[start_node] = 1

    # create min heap to store minimum edge data
    candidate = graph[start_node]
    heapq.heapify(candidate)

    mst = []
    total_weight = 0

    while candidate:
        weight, u, v = heapq.heappop(candidate)
        if visited[v] == 0: # run only when the node is not visited
            visited[v] = 1
            mst.append((u, v))
            total_weight += weight

            for edge in graph[v]: # add candidate edges to the heap if end node is not visited
                if visited[edge[2]] == 0:
                    heapq.heappush(candidate, edge)

    return total_weight

print(prim(graph, 1))