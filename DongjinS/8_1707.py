# 8	1707	중	DFS	이분 그래프
'''
문제
그래프의 정점의 집합을 둘로 분할하여, 
각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때,
그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.

그래프가 입력으로 주어졌을 때,
이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.

입력
입력은 여러 개의 테스트 케이스로 구성되어 있는데,
첫째 줄에 테스트 케이스의 개수 K가 주어진다.
각 테스트 케이스의 첫째 줄에는 그래프의 정점의 개수 V와 간선의 개수 E가 빈 칸을 사이에 두고 순서대로 주어진다.
각 정점에는 1부터 V까지 차례로 번호가 붙어 있다.
이어서 둘째 줄부터 E개의 줄에 걸쳐 간선에 대한 정보가 주어지는데, 각 줄에 인접한 두 정점의 번호 u, v (u ≠ v)가 빈 칸을 사이에 두고 주어진다. 

출력
K개의 줄에 걸쳐 입력으로 주어진 그래프가 이분 그래프이면 YES, 아니면 NO를 순서대로 출력한다.
'''
from sys import stdin, setrecursionlimit
from collections import defaultdict, deque

def BFS(start_node, color):
    que = deque()
    que.append(start_node)
    colorchk[start_node] = color

    while que:
        v = que.popleft()
        for node in edge[v]:
            if colorchk[node] == 0:
                que.append(node)
                colorchk[node] = colorchk[v] * -1
            elif colorchk[node] == colorchk[v]:
                return 0
    return 1

K = int(stdin.readline())

for _ in range(K):
    V, E = [int(x) for x in stdin.readline().split()]
    edge = defaultdict(list)
    # 색 칠하기 - 방문확인과 비슷, 기본값 0 -> 방문하면 1 or -1 로 칠해줌
    colorchk = [0] * (V+1)
    check_divide = 1
    for _ in range(E):
        u, v = [int(x) for x in stdin.readline().split()]
        edge[u].append(v)
        edge[v].append(u)

    for node in edge:
        #이분그래프 아니면 스탑
        if check_divide == 0:
            break
        
        #방문하지 않은 = 색칠 되지 않은(=0) 노드만 탐색 시작
        if colorchk[node] == 0:
            check_divide = BFS(node, 1)
    
    if check_divide == 1:
        print("YES")
    else:
        print("NO")
