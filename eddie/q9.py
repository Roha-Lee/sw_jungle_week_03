import collections
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

N = int(input())
indoor = ['0'] + list(input().strip())
for i in range(len(indoor)):
    indoor[i] = int(indoor[i])

graph = collections.defaultdict(list)

for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0
count2 = 0
### Imporved performance
visited = [0] * (N + 1)

def dfs(node):
    global count
    global count2

    if indoor[node] == 0:

        if visited[node] == 1:
            return

        visited[node] = 1

        neighbors = graph[node]

        for next in neighbors:
            if indoor[next] == 1:
                count += 1
                dfs(next)
            else:
                dfs(next)
    else:
        if visited[node] == 1:
            return

        neighbors = graph[node]

        visited[node] = 1

        for next in neighbors:
            if indoor[next] == 1 and visited[next] == 0:
                count2 += 1
                dfs(next)

paths = 0

if all(indoor[1:]) == True: # if there are only indoor nodes
    count2 = 0
    dfs(i)
    paths += count2 * 2
else: # if there are at least one outdoor node
    for i in range(1, N + 1):
        count = 0
        count2 = 0
        if indoor[i] == 0 and visited[i] == 0:
            dfs(i)

        paths += count * (count - 1)
        paths += count2 * 2

print(paths)

### Original version
# def dfs(node):
#     global count

#     if visited[node] == 1:
#         return

#     visited[node] = 1
#     neighbors = graph[node]

#     for next in neighbors:
#         if indoor[next] == '1' and visited[next] == 0:
#             visited[next] = 1
#             count += 1
#         else:
#             dfs(next)

# for i in range(1, N + 1):
#     if indoor[i] == '1':
#         visited = [0] * (N + 1)
#         dfs(i)

# print(count)