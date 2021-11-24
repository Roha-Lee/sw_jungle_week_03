# 18	3055	중	BFS	탈출
'''
문제
사악한 암흑의 군주 이민혁은 드디어 마법 구슬을 손에 넣었고, 그 능력을 실험해보기 위해 근처의 티떱숲에 홍수를 일으키려고 한다.
이 숲에는 고슴도치가 한 마리 살고 있다. 고슴도치는 제일 친한 친구인 비버의 굴로 가능한 빨리 도망가 홍수를 피하려고 한다.

티떱숲의 지도는 R행 C열로 이루어져 있다. 비어있는 곳은 '.'로 표시되어 있고, 물이 차있는 지역은 '*', 돌은 'X'로 표시되어 있다.
비버의 굴은 'D'로, 고슴도치의 위치는 'S'로 나타내어져 있다.

매 분마다 고슴도치는 현재 있는 칸과 인접한 네 칸 중 하나로 이동할 수 있다.
(위, 아래, 오른쪽, 왼쪽) 물도 매 분마다 비어있는 칸으로 확장한다.
물이 있는 칸과 인접해있는 비어있는 칸(적어도 한 변을 공유)은 물이 차게 된다.
물과 고슴도치는 돌을 통과할 수 없다. 또, 고슴도치는 물로 차있는 구역으로 이동할 수 없고, 물도 비버의 소굴로 이동할 수 없다.

티떱숲의 지도가 주어졌을 때, 고슴도치가 안전하게 비버의 굴로 이동하기 위해 필요한 최소 시간을 구하는 프로그램을 작성하시오.

고슴도치는 물이 찰 예정인 칸으로 이동할 수 없다. 즉, 다음 시간에 물이 찰 예정인 칸으로 고슴도치는 이동할 수 없다.
이동할 수 있으면 고슴도치가 물에 빠지기 때문이다. 

입력
첫째 줄에 50보다 작거나 같은 자연수 R과 C가 주어진다.

다음 R개 줄에는 티떱숲의 지도가 주어지며, 문제에서 설명한 문자만 주어진다. 'D'와 'S'는 하나씩만 주어진다.

출력
첫째 줄에 고슴도치가 비버의 굴로 이동할 수 있는 가장 빠른 시간을 출력한다. 만약, 안전하게 비버의 굴로 이동할 수 없다면, "KAKTUS"를 출력한다.
'''
## 물도 한큐에 털고 고슴도치도 한큐에 턴다!
#한큐에 털어야 했던 이유 - 한 턴(while 힌번 반복) 안에서 물 큐, 고슴도치 큐에서 각각 하나씩 빠지고 늘어나고 하면 큐의 순서에 따라 물보다 고슴도치가 먼저 이동하게 된다.
# - 한 턴마다 큐에 있던걸 먼저 다 털고 나면 물이 갈 수 있는 모든 곳을 선점하게 되고 그 후에 고슴도치가 이동할 곳을 고를 수 있다.
# visited 없어도 통과,,
from sys import stdin
from collections import deque

def BFS(water_q, s_q):
    #물과 비버가 이동할 수 있는지 확인하기 위한 상하좌우 좌표
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    # 물 큐, 고슴도치 큐 둘 중 하나라도 남아있다면 while 유지
    while water_q or s_q:
        # 물큐 있다면
        if water_q:
            # 이미 큐안에 들어 있는 물의 위치들 다 털때 까지 반복
            for _ in range(len(water_q)):
                #현재 물의 위치 - wx, wy
                wx, wy = water_q.popleft()
                # 상하좌우 물이 갈 수 있는 곳 확인
                for i in range(4):
                    # 새로 물이 들어갈 위치 - nwx, nwy
                    nwx, nwy = wx+dx[i], wy+dy[i]
                    # 새로 물이들어갈 위치가 숲 지도의 범위 안에 있고
                    if 0 <= nwx < R and 0 <= nwy < C:
                        # 0이라면 - 물이 들어갈 수 있는 지역이라면
                        if forest_map[nwx][nwy] == 0:
                            # 물이 들어 간 지역은 -1 로 바꾸고 새로 물이 들어간 위치 물 큐에 넣는다.
                            forest_map[nwx][nwy] = -1
                            water_q.append((nwx,nwy))
        # 고슴도치 큐 있다면
        if s_q:
            # 이미 큐안에 들어 있는 고슴도치의 위치 다 털때까지 반복
            for _ in range(len(s_q)):
                # 현재 고슴도치의 위치 - sx, sy
                sx, sy = s_q.popleft()
                #상하좌우 고슴도치가 들어갈 수 있는 곳 확인
                for i in range(4):
                    # 새로운 고슴도치의 이동 위치 - nsx, nsy
                    nsx, nsy = sx+dx[i], sy+dy[i]
                    # 새로온 고슴도치의 위치가 숲 지도의 범위 안이고
                    if 0 <= nsx < R and 0 <= nsy < C:
                        # 새로운 고슴도치의 위치가 이동할 수 있는 위치 - 0 혹은 비버의집 - D 라면
                        if forest_map[nsx][nsy] == 0 or forest_map[nsx][nsy] == "D":
                            # 고슴도치가 이동한 위치는 현재 고슴도치가 있던 위치의 값에 + 1 한 값을 넣는다 
                            # = 고슴도치가 새로운 위치로 갈 수 있는 최소시간
                            # 새로운 고슴도치의 위치 고슴도치 큐에 넣는다.
                            forest_map[nsx][nsy] = forest_map[sx][sy] + 1
                            s_q.append((nsx,nsy))

# 숲 지도의 행 - R, 열 - C        
R, C = [int(x) for x in stdin.readline().split()]
# 숲 지도 - forest_map
forest_map = []
for _ in range(R):
    forest_map.append(list(stdin.readline().strip()))
# 물 큐 - water_q 와 고슴도치 큐 - s_q 만들어주고 시작점 넣어주기
water_q = deque()
s_q = deque()
# 비버 집 좌표 저장 - beaver_house
beaver_house = ()
for i in range(R):
    for j in range(C):
        # 숲 지도의 고슴도치 위치 1로 바꾸고 & s_q에 넣기
        if forest_map[i][j] == "S":
            forest_map[i][j] = 1
            s_q.append((i,j))
        # 숲 지도의 물 시작점 water_q에 넣어주기
        elif forest_map[i][j] == "*":
            water_q.append((i,j))
        # 숲 지도의 비버 집 위치 저장
        elif forest_map[i][j] == "D":
            beaver_house = (i,j)
        # 숲 지도의 물이 찰 수 있거나 고슴도치가 이동할 수 있는 위치 . -> 0 으로 바꿔주기
        elif forest_map[i][j] == ".":
            forest_map[i][j] = 0
#BFS 시작 - 물이 차는 동안 고슴도치가 비버의 집에 몇번 만에 도착할 수 있는지 계산
BFS(water_q, s_q)
#고슴도치가 비버 집에 도착했다면 = 숲속 지도의 비버 집 위치의 값이 D->숫자로 바꼈다면, 비버집 위치의 값 - 1이 고슴도치가 도달하는데 걸린 시간
if str(forest_map[beaver_house[0]][beaver_house[1]]).isdigit():
    print(forest_map[beaver_house[0]][beaver_house[1]]-1)
# 도착하지 못했다면 = 비버집의 값이 숫자가 아니라면 KAKTUS 출력
else:
    print("KAKTUS")
