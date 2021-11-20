# 5	11724	하	그래프 탐색 기본	연결 요소의 개수
'''
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
3 초	512 MB	53746	25315	16532	44.020%
문제
방향 없는 그래프가 주어졌을 때,
연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. 
(1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다.
(1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

출력
첫째 줄에 연결 요소의 개수를 출력한다.

DFS로도 구현해보기
'''
# 유니온, 파인드 사용
from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)

def find(target):
    if parent[target] == target:
        return target
    else:
        parent[target] = find(parent[target])
        return parent[target]

def union(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    elif x<y:
        parent[y] = x
    else:
        parent[x] = y


# 정점의 개수 N과 간선의 개수 M
N, M = [int(x) for x in stdin.readline().split()]

edge = []
for i in range(M):
    u, v = [int(x) for x in stdin.readline().split()]
    edge.append([u,v])
    edge.append([v,u])
    
parent = list(range(N+1))

edge.sort()
for u,v in edge:
    if find(u) != find(v):
        union(u,v)

tmp = [0]
ans = 0
for i in parent:
    if i not in tmp:
        ans += 1
        tmp.append(i)
print(ans)