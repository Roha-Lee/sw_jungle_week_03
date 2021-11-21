# 9	21606	중	DFS	아침 산책
'''
문제
아침 산책을 즐기는 서현이는 서울과학고에 입학해서도 아침 산책을 즐기려고 합니다.
서현이는 산책을 위해 서울과학고의 지리를 분석했고, 그 결과 서울과학고를 N개의 장소를 N-1개의 길이 잇는 트리 형태로 단순화시킬 수 있었습니다.
트리 구조이므로, 모든 장소를 몇 개의 길을 통해 오고갈 수 있습니다.

아침 산책은 시작점과 도착점을 정하고, 시작점에서 도착점까지 트리 위의 단순 경로(같은 점을 여러 번 지나지 않는 경로)를 따라 걷게 됩니다.
트리 위의 두 점 사이의 경로는 유일하므로 시작점과 도착점이 정해지면 경로는 유일하게 결정됩니다.

N개 장소 중에 일부 장소는 실내이며, 나머지 장소는 실외입니다.
서현이는 산책을 시작하기 전부터 운동을 하는 것을 원치 않기 때문에, 산책의 시작점과 끝점은 모두 실내여야 합니다.
또한, 산책 도중에 실내 장소를 만나면 산책을 그만두고자 하는 욕구가 생기기 때문에, 산책 경로 위에 시작점과 끝점을 제외하고 실내 장소가 있으면 안 됩니다.

서현이는 매일 다른 산책 경로를 걷고자 합니다. 서로 다른 산책 경로가 몇 가지 있는지 구해 봅시다.

입력
첫 줄에는 정점의 수 N이 주어집니다.

둘째 줄에는 1과 0으로 이루어진 길이 N의 문자열 A가 주어집니다.
i번째 문자 A_i가 1일 경우 i번 장소는 실내이며, 0 경우 $i$번 장소는 실외입니다.

셋째 줄부터 N+1번 줄까지는 i+2번 줄에 트리의 각 간선을 나타내는 두 정수 u_i, v_i가 주어집니다.
이는 i번째 간선이 u_i번 정점과 v_i번 정점을 연결한다는 의미입니다.

출력
가능한 서로 다른 산책 경로의 수를 출력합니다.
'''
from sys import stdin, setrecursionlimit
from collections import defaultdict
setrecursionlimit(10**9)

def DFS_1(start, res):
    for child in edge[start]:
        if visited[child] == 0 and  A[child] == 1:
            res += 1
    return res

def DFS_2(start, res):
    for child in edge[start]:
        if visited[child] == 0 and A[child]!= 1:
            visited[child] = 1
            res = DFS_2(child, res)
            A[child] = 2
        elif visited[child] == 0 and  A[child] == 1:
            res += 1
    return res


#정점의 수 N, 정점이 실내=1인지 실외=1인지 A
N = int(stdin.readline())
A = list(map(int,'0'+stdin.readline().strip()))

#간선 정보 - edge
edge = defaultdict(list)
for _ in range(N-1):
    u, v = [int(x) for x in stdin.readline().split()]
    edge[u].append(v)
    edge[v].append(u)

#실외에서 부터 세는 방식
#1. 실외에서 이어지는 실내 개수 세기 
total = 0
for start in edge:
    # 시작점이 실외면 dfs 시작.
    #res2 - 실외와 연결된 실내의 개수.
    res2 = 0
    if A[start] == 0:    
        #경로 탐색시 방문 확인 - visited
        visited = [0] * (N+1)
        visited[start] = 1
        A[start] = 2
        res2 = DFS_2(start, res2)
        total = total + res2*(res2-1)

print(edge, A)

#2. 실내 - 실내 경로 개수 세기
#위의 반복문 끝나고 나면 실내는 전부 1이되고 실외는 2가됨 - 1 실내에서 출발해서 바로 1로 끝나는 애들만 세주면 됨
for start in edge:
    # 시작점이 실외면 dfs 시작.
    #res2 - 실외와 연결된 실내의 개수.
    res2 = 0
    if A[start] == 1:    
        #경로 탐색시 방문 확인 - visited
        visited = [0] * (N+1)
        visited[start] = 1
        res2 = DFS_1(start, res2)
        total = total + res2

print(total)


#실내에서 부터 세는 방식
# res = 0
# for start in edge:
#     # 시작점이 실내이면 dfs 시작.
#     if A[start] == 1:    
#         #경로 탐색시 방문 확인 - visited
#         visited = [0] * (N+1)
#         visited[start] = 1
#         res = DFS_1(start, res)

# print(res)