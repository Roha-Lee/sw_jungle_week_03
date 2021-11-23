# 22	1432	상	위상 정렬	그래프 수정
'''
문제
N개의 정점이 있는 그래프가 주어지면, 다음과 같은 방법에 의해서 정점의 번호를 다시 매기고 싶다.

모든 그래프의 번호는 1보다 크거나 같고 N보다 작거나 같은 번호를 가져야 한다.

만약 V1에서 V2로 연결된 간선이 있다면, V2의 번호는 V1보다 커야 한다.

위와 같은 조건을 이용해서 그래프의 번호를 다시 매긴 후에,
1번 정점의 새로 고친 번호를 M1, 2번 정점의 새로 고친 번호를 M2, ..., N번 정점의 새로 고친 번호를 MN이라고 하면, N개의 수열이 만들어진다.

이 수열을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N이 주어진다. 둘째 줄부터 N개의 줄에는 인접행렬 형식으로 입력이 주어진다.
0은 연결되지 않았음을 의미하고, 1은 연결되었다는 것을 의미한다. N은 50보다 작거나 같은 자연수이다.

출력
첫째 줄에 수열의 각 원소를 차례대로 공백을 사이에 두고 출력한다.
만약 그래프의 번호를 수정할 수 없다면 -1을 출력한다.
답이 여러 개일 경우에는 사전 순으로 제일 앞서는 것을 출력한다.
'''
## 그래프를 정방향으로 해서 위상정렬할 시 같은 차수의 두개의 정점을 골라야 할때 아웃워드 차수가 높고 정점의 숫자가 낮은 것을 골라야한다.
# 이런 조건 속에서 위상정렬을 수행하기 어렵기 때문에 역방향으로 그래프를 바꾸어 조건 또한 반대로 같은 차수의 두개의 정점을 골라야 할때 인워드 차수가 낮고 정점의 숫자가 높은 것을 고르면된다.
# 이러한 조건은 정상적인 위상정렬을 통해 인워드차수가 낮은걸 큐에 넣어 구해주면 되고 우선순위 큐를 통해 정점의 숫자가 높은 것(- 붙이기)을 고르면 된다.
# 그렇게 역으로 만든 그래프를 통해 위상정렬을 하여 나온 결과를 다시 리버스하고 zip 함수를 통해 인덱스를 붙여준다.
# 이것을 다시 결과 순으로 정렬하면 결과는 정렬되고 인덱스는 결과를 따라 바뀌게 된다. 이때의 인덱스 값이 답이다.
from sys import stdin
from collections import deque, defaultdict
from heapq import heappush, heappop
def topology(N, connected_info):
    #진입 차수 구하기(원본의 아웃워드 디그리)    
    indegree = {i:0 for i in range(1,N+1)}
    for key in connected_info:
        for i in connected_info[key]:
            indegree[i] += 1
    # print(indegree)
    #indegree 0 이면 우선순위큐에 넣기
    hq = []
    for i in indegree:
        if indegree[i] == 0:
            heappush(hq,-i)
    # print(hq)
    #위상정렬 진행
    res = []
    while hq:
        now = -(heappop(hq))
        res.append(now)
        for next in connected_info[now]:
            indegree[next] -= 1
            if indegree[next] == 0:
                heappush(hq,-next)
    # print(res)
    if len(res) == N:
        #위상정렬된 것들 뒤집고 원래 인덱스 구하기
        res.reverse()
        # print(res)
        # print(sorted(list(zip(res, range(1,N+1)))))
        # print(*sorted(list(zip(res, range(1,N+1)))))
        res, index = (zip(*sorted(list(zip(res, range(1,N+1))))))
        print(*index)
        return
    else:
        print(-1)
        return
N = int(stdin.readline())
connected_info = defaultdict(list)
flag_2_topology = 0
for i in range(N):
    tmp = list(map(int,stdin.readline().strip()))
    for j in range(N):
        if tmp[j] == 1:
            connected_info[j+1].append(i+1)
            if j<i:
                flag_2_topology = 1
# print(connected_info)
if flag_2_topology == 0:
    print("위상정렬 안해도됨")
    print(*[i for i in range(1,N+1)])
else:
    topology(N, connected_info)
