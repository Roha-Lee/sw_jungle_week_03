from collections import defaultdict
import sys 
sys.setrecursionlimit(100000000)
def find_parent(tree, parent, visited, node = 1):
    for child in tree[node]: 
        if not visited[child]:       
            parent[child] = node
            visited[child] = True
            find_parent(tree, parent, visited, child)
    return parent
    
if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    tree = defaultdict(list)
    parent = [i for i in range(0, n+1)]
    visited = [False] * (n+1)
    for _ in range(n-1):
        src, dst = map(int, input().split())
        tree[src].append(dst)
        tree[dst].append(src)
    
    visited[1] = True
    parent = find_parent(tree, parent, visited)
    print(*parent[2:], sep='\n')