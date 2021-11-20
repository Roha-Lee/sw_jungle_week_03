# 7	11725	중	DFS	트리의 부모 찾기
'''
문제
루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때,
각 노드의 부모를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다.
둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

출력
첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.
'''
from sys import stdin, setrecursionlimit
from typing import DefaultDict
from collections import defaultdict
setrecursionlimit(10**9)

def DFS(root):
    for node in edge[root]:
        if visited[node] != True:
            parent[node] = root
            visited[node] = True
            DFS(node)
    return



N = int(stdin.readline())

edge = defaultdict(list)

parent = list(range(N+1))
visited = [False] * (N+1)

for i in range(N-1):
    a, b =[int(x) for x in stdin.readline().split()]
    edge[a].append(b)
    edge[b].append(a)

DFS(1)
print(*parent[2:], sep="\n")