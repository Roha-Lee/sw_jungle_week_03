# 3	1197	하	그래프 탐색 기본	최소 스패닝 트리
'''
문제
그래프가 주어졌을 때, 그 그래프의 최소 스패닝 트리를 구하는 프로그램을 작성하시오.

최소 스패닝 트리는, 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리를 말한다.

입력
첫째 줄에 정점의 개수 V(1 ≤ V ≤ 10,000)와 간선의 개수 E(1 ≤ E ≤ 100,000)가 주어진다.
다음 E개의 줄에는 각 간선에 대한 정보를 나타내는 세 정수 A, B, C가 주어진다. 
이는 A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있다는 의미이다. 
C는 음수일 수도 있으며, 절댓값이 1,000,000을 넘지 않는다.

그래프의 정점은 1번부터 V번까지 번호가 매겨져 있고, 임의의 두 정점 사이에 경로가 있다.
최소 스패닝 트리의 가중치가 -2,147,483,648보다 크거나 같고, 2,147,483,647보다 작거나 같은 데이터만 입력으로 주어진다.

출력
첫째 줄에 최소 스패닝 트리의 가중치를 출력한다.
'''
from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)

#부모 - root 를 찾는 함수
def find(target):
    if parent[target] == target:
        return target
    else:
        parent[target] = find(parent[target])
        return parent[target]

#간선을 하나로 합치는? 이어주는 함수
def union(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    elif x<y:
        parent[y] = x
    else:
        parent[x] = y



#V - 정점의 개수 E - 간선의 개수
V, E = [int(x) for x in stdin.readline().split()]
parent = list(range(V+1))

edges = []
for _ in range(E):
    A,B,C = [int(x) for x in stdin.readline().split()]
    edges.append([A,B,C])

edges.sort(key=lambda x:x[2])

ans = 0
for a,b,c in edges:
    if find(a) != find(b):
        union(a,b)
        ans+=c

print(ans)