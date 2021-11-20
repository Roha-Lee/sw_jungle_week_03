# 6	2606	하	그래프 탐색 기본	바이러스
'''
문제
신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다.
한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.

예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자.
1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 전파되어
2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다.
하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.

어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에는 컴퓨터의 수가 주어진다.
컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다.
둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다.
이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.

출력
1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.

반례 - https://www.acmicpc.net/board/view/68097

for c1, c2 in com_pair:
    if find(c1) != find(c2):
        union(c1,c2)
한번 더 해줘서 해결... 더 깔끔한 방법 생각해보기..

DFS러 구현해보기
'''
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

com_n = int(stdin.readline())
connect_n = int(stdin.readline())

com_pair = []
for i in range(connect_n):
    c1,c2 = [int(x) for x in stdin.readline().split()]
    com_pair.append([c1,c2])
    com_pair.append([c2,c1])

com_pair.sort()
parent = list(range(com_n+1))

print(com_pair)
print(parent)

for c1, c2 in com_pair:
    if find(c1) != find(c2):
        union(c1,c2)

for c1, c2 in com_pair:
    if find(c1) != find(c2):
        union(c1,c2)


print("///////////////")
print(parent)

ans = 0
for i in parent:
    if i == 1:
        ans+=1
print(ans-1)
