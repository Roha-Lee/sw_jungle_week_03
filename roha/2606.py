import sys 
from collections import defaultdict
from collections import deque
def get_infected_computers(com, networks, root = 1, result = []):
    q = deque([root])
    visited = [False] * (com + 1)

    while q: 
        curr = q.popleft()
        if visited[curr]:
            continue
        
        visited[curr] = True
        result.append(curr)
        for next_node in networks[curr]:
            if not visited[next_node]:
                q.append(next_node)
    
    return result
    

if __name__ == '__main__':
    input = sys.stdin.readline
    com = int(input())
    num = int(input())
    networks = defaultdict(list)
    for _ in range(num):
        src, dst = map(int, input().split())
        networks[src].append(dst)
        networks[dst].append(src)
    print(len(get_infected_computers(com, networks))-1)
