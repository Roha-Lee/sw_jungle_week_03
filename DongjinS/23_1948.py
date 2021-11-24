# 23	1948	상	위상 정렬	임계경로
'''
문제
월드 나라는 모든 도로가 일방통행인 도로이고, 싸이클이 없다.
그런데 어떤 무수히 많은 사람들이 월드 나라의 지도를 그리기 위해서,
어떤 시작 도시로부터 도착 도시까지 출발을 하여 가능한 모든 경로를 탐색한다고 한다.

이 지도를 그리는 사람들은 사이가 너무 좋아서 지도를 그리는 일을 다 마치고 도착 도시에서 모두 다 만나기로 하였다.
그렇다고 하였을 때 이들이 만나는 시간은 출발 도시로부터 출발한 후 최소 몇 시간 후에 만날 수 있는가?
즉, 마지막에 도착하는 사람까지 도착을 하는 시간을 의미한다.

어떤 사람은 이 시간에 만나기 위하여 1분도 쉬지 않고 달려야 한다.
이런 사람들이 지나는 도로의 수를 카운트 하여라.

출발 도시는 들어오는 도로가 0개이고, 도착 도시는 나가는 도로가 0개이다.

입력
첫째 줄에 도시의 개수 n(1 ≤ n ≤ 10,000)이 주어지고 둘째 줄에는 도로의 개수 m(1 ≤ m ≤ 100,000)이 주어진다.
그리고 셋째 줄부터 m+2줄까지 다음과 같은 도로의 정보가 주어진다.
처음에는 도로의 출발 도시의 번호가 주어지고 그 다음에는 도착 도시의 번호, 그리고 마지막에는 이 도로를 지나는데 걸리는 시간이 주어진다.
도로를 지나가는 시간은 10,000보다 작거나 같은 자연수이다.

그리고 m+3째 줄에는 지도를 그리는 사람들이 출발하는 출발 도시와 도착 도시가 주어진다.

모든 도시는 출발 도시로부터 도달이 가능하고, 모든 도시로부터 도착 도시에 도달이 가능하다.

출력
첫째 줄에는 이들이 만나는 시간을, 둘째 줄에는 1분도 쉬지 않고 달려야 하는 도로의 수가 몇 개인지 출력하여라.
'''
from sys import stdin
from collections import defaultdict, deque
N = int(stdin.readline())
M = int(stdin.readline())

world_map = defaultdict(list)
back_world_map = defaultdict(list)

#정방향으로의 그래프 관계 - world_map, 과 역방향으로의 그래프 관계 - back_world_map을 만든다.
for _ in range(M):
    u,v,d = [int(x) for x in stdin.readline().split()]
    world_map[u].append((v, d))
    back_world_map[v].append((u,d))

#출발점과 목적지를 입력
start, end = [int(x) for x in stdin.readline().split()]

indegree = {i:0 for i in range(1,N+1)}

#정방향 그래프에서의 각 정점별 진입차수를 만든다. indegree
for departure in world_map:
    for arrival, dist in world_map[departure]:
        indegree[arrival] += 1

#위상정렬 시작
#정점 별 최대거리 찾기
q = deque()
q.append((0,start))
city_maxdist = {i:0 for i in range(1,N+1)}

while q:
    now_dist, now_city = q.popleft()
    for next_city, next_dist in world_map[now_city]:
        #현재 지점까지의 거리(최대거리)와 이동할 거리를 더한 것과 이동할 지점의 현재 최대 거리를 비교해서 이동할 지점까지의 최대 거리를 최신화
        city_maxdist[next_city] = max(city_maxdist[next_city], now_dist + next_dist)
        #진입 차수가 0이 된 것들은 큐에 넣는다 = 정점(next_city)까지의 최대거리가 확정된 것들 - 더 이상 최신화할 진입이 없는 것들.
        indegree[next_city] -= 1
        if indegree[next_city] == 0:
            q.append((city_maxdist[next_city], next_city))

ans_dist = city_maxdist[end]
print(ans_dist)

#최대거리 가능한 간선 개수 구하기
q.append((ans_dist, end))
visited = set()
while q:
    now_dist, now_city = q.popleft()
    for next_city, next_dist in back_world_map[now_city]:
        if (now_city, next_city) not in visited:
            #현재까지의 최대거리(now_dist)에서 이동할 지점까지의 거리를 뺀 게 이동할 지점의 최대거리인지 확인 - 목적지의 최대치를 도달하는 경로인지 확인
            if city_maxdist[next_city] == now_dist - next_dist:
                #확인된 경로의 (정정의 최대거리와 정점)을 큐에 넣고, 방문한 경로에도 (현재 정점, 확인된 이동한 정점)넣어서 같은 경로를 다시 반복하지 않게 한다
                q.append((city_maxdist[next_city], next_city))
                visited.add((now_city, next_city))

#확인된 경로의 숫자 = 목적지까지 최대거리로 도달할 수 있는 경로의 숫자
print(len(visited))