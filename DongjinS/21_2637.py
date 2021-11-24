# 21	2637	중	위상 정렬	장난감조립
'''
문제
우리는 어떤 장난감을 여러 가지 부품으로 조립하여 만들려고 한다.
이 장난감을 만드는데는 기본 부품과 그 기본 부품으로 조립하여 만든 중간 부품이 사용된다.
기본 부품은 다른 부품을 사용하여 조립될 수 없는 부품이다. 중간 부품은 또 다른 중간 부품이나 기본 부품을 이용하여 만들어지는 부품이다.

예를 들어보자. 기본 부품으로서 1, 2, 3, 4가 있다. 중간 부품 5는 2개의 기본 부품 1과 2개의 기본 부품 2로 만들어진다.
그리고 중간 부품 6은 2개의 중간 부품 5, 3개의 기본 부품 3과 4개의 기본 부품 4로 만들어진다.
마지막으로 장난감 완제품 7은 2개의 중간 부품 5, 3개의 중간 부품 6과 5개의 기본 부품 4로 만들어진다.
이런 경우에 장난감 완제품 7을 만드는데 필요한 기본 부품의 개수는 1번 16개, 2번 16개, 3번 9개, 4번 17개이다.

이와 같이 어떤 장난감 완제품과 그에 필요한 부품들 사이의 관계가 주어져 있을 때 하나의 장난감 완제품을 조립하기 위하여 필요한 기본 부품의 종류별 개수를 계산하는 프로그램을 작성하시오.

입력
첫째 줄에는 자연수 N(3 ≤ N ≤ 100)이 주어지는데, 1부터 N-1까지는 기본 부품이나 중간 부품의 번호를 나타내고, N은 완제품의 번호를 나타낸다.
그리고 그 다음 줄에는 자연수 M(3 ≤ M ≤ 100)이 주어지고, 그 다음 M개의 줄에는 어떤 부품을 완성하는데 필요한 부품들 간의 관계가 3개의 자연수 X, Y, K로 주어진다.
이 뜻은 "중간 부품이나 완제품 X를 만드는데 중간 부품 혹은 기본 부품 Y가 K개 필요하다"는 뜻이다. 두 중간 부품이 서로를 필요로 하는 경우가 없다.

출력
하나의 완제품을 조립하는데 필요한 기본 부품의 수를 한 줄에 하나씩 출력하되(중간 부품은 출력하지 않음),
반드시 기본 부품의 번호가 작은 것부터 큰 순서가 되도록 한다.
각 줄에는 기본 부품의 번호와 소요 개수를 출력한다.

정답은 2,147,483,647 이하이다.
'''
## https://velog.io/@qweadzs/BOJ-2637-%EC%9E%A5%EB%82%9C%EA%B0%90-%EC%A1%B0%EB%A6%BDPython
from sys import stdin
from collections import defaultdict, deque
#부품의 개수 - N
N = int(stdin.readline())
# 중간 혹은 완제품을 완성하는데 필요한 부품의 관계 수  - M 
M = int(stdin.readline())
# 중간 혹은 완제품을 완성하는데 필요한 부품의 관계 - requirement_info
requirement_info = defaultdict(list)
# 부품을 만드는데 필요한 부분 부품의 단순 개수를 저장 = 진입차수 - indegree
# -> (5:2, 6:3, 7:3)
indegree = [0] * (N+1)
# 중간 혹은 완제품을 만드는데 필요한 '기본' 부품들의 개수를 저장 - part_cnt
# -> (5:[2,2,0,0,0,0,0], 6:[2*2,2*2,3,4,0,0,0], 7:[2*2+(2*2)*3, 2*2+(2*2)*3, 3*3, 5+4*3, 0, 0, 0])
part_cnt = [[0]* (N+1) for _ in range(N+1)]
for _ in range(M):
    u,v,c = [int(x) for x in stdin.readline().split()]
    requirement_info[v].append((u,c))
    indegree[u] += 1
# indegree 0인 부품들을 큐에 넣는다 - 1,2,3,4
q = deque()
for i in range(1,len(indegree)):
    if indegree[i] == 0:
        q.append(i)
## 직전 문제에서는 n번 반복(사이클이 있는지 파악) 여기서는 중요하지 않은 이유.
# - 만들기 위해 1번 부품을 필요로하는 N번 부품이 1번 부품을 만들기위해 필요로 되지 않는다면 사이클 없는 것.
while q:
    now = q.popleft()
    # now를 필요로 하는 'node'와 node 가 now를 필요로 하는 개수 'need'
    for node, need in requirement_info[now]:
        # now가 기본 부품이면 (part count 의 now 행의 모든 열이 0이면 기본부품) node의 해당하는 part_cnt의 행열(part[node][now])에 now를 필요로 하는 만큼만(need) 더해준다
        # 시작을 기본 부품으로 하기 때문에 처음 큐에 들어온 기본 부품들을 큐에서 빼면서 part_cnt 의 중간+완제품 행에는 0이 아닌 것들이 생기게 된다.
        if part_cnt[now].count(0) == N+1:
            part_cnt[node][now] += need
        # now가 중간 부품이면 node의 해당하는 part_cnt의 행에 now에 해당하는 part_cnt의 모든 열을 필요한(need) 만큼 곱해서 더해준다.
        else:
            for i in range(1,len(part_cnt)):
                part_cnt[node][i] += part_cnt[now][i] * need
        # node가 필요로 하는 now의 부품을 채워주었기 때문에 node의 진입차수를 -1 해준다. 
        indegree[node]-=1
        # node의 진입 차수가 0이 되면(=필요한 부품이 모두 채워졌으면) 큐에 node를 넣어준다.
        if indegree[node] == 0:

            q.append(node)
# N = 완제품 = 마지막 제품 번호 의 part_cnt 행의 0을 제외한(기본 부품들의) 모든 값을 한개씩 출력해준다.
for i in range(1,len(part_cnt[N])):
    if part_cnt[N][i]:
        print(i, part_cnt[N][i])
