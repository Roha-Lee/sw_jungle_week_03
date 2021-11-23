# 20	2252	하	위상 정렬	줄 세우기
'''
문제
N명의 학생들을 키 순서대로 줄을 세우려고 한다.
각 학생의 키를 직접 재서 정렬하면 간단하겠지만, 마땅한 방법이 없어서 두 학생의 키를 비교하는 방법을 사용하기로 하였다.
그나마도 모든 학생들을 다 비교해 본 것이 아니고, 일부 학생들의 키만을 비교해 보았다.

일부 학생들의 키를 비교한 결과가 주어졌을 때, 줄을 세우는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 32,000), M(1 ≤ M ≤ 100,000)이 주어진다. M은 키를 비교한 회수이다.
다음 M개의 줄에는 키를 비교한 두 학생의 번호 A, B가 주어진다. 이는 학생 A가 학생 B의 앞에 서야 한다는 의미이다.

학생들의 번호는 1번부터 N번이다.

출력
첫째 줄에 학생들을 키 순서대로 줄을 세운 결과를 출력한다. 답이 여러 가지인 경우에는 아무거나 출력한다.
'''
#위상 정렬, - https://www.youtube.com/watch?v=qzfeVeajuyc
# 각 정점의 연결 관계와 각 정점 진입에 필요한 조건(차수)를 저장하고 차수가 0인 정점 부터 큐에 넣는다.
# q에서 하나씩 pop하면서 팝된 정점이 진입 조건인 정점의 차수를 -1 한다. 차수가 0 이된 정점을 다시 큐에 넣는다.
# 이 과정을 반복하며 q에서 나온 순서가 위상정렬된 순서이다.
# 정점의 개수만큼 팝이 되어야 하기 때문에 정점의 개수만큼 반복하고 그 전에 큐가 비게 되면 그래프안에 사이클이 있는것으로 위상정렬을 할 수 없는 그래프 이다.
from sys import stdin
from collections import deque, defaultdict
N, M = [int(x) for x in stdin.readline().split()]

indegree = [0] * (N+1)
height_compare = defaultdict(list)

for _ in range(M):
    u,v = [int(x) for x in stdin.readline().split()]
    indegree[v] += 1
    height_compare[u].append(v)


res = []
q = deque()
for i in range(1,len(indegree)):
    if indegree[i] == 0:
        q.append(i)

for _ in range(N):
    if not q:
        print('cycle, cannor topology')
    x = q.popleft()
    res.append(x)
    for node in height_compare[x]:
        indegree[node]-=1
        if indegree[node] == 0:
            q.append(node)

    
print(*res, sep=" ")
