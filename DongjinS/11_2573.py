# 11	2573	상	DFS	빙산
from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)
#얼음 녹이기 함수
def MeltingIce(x,y,cnt, visited):
    ## 상하좌우 확인하면서(안전영역 이랑 비슷하게) 0이면 -1 아면 0이 아니면 자기자신 방문 확인하고 재귀들어가는 방식으로 바꿔야함.
    ## 함수 밖에서 반복문으로 방문확인 안된 곳부터 시작해서 방문확인하면서 상하좌우로 0체크해서 -1 하고 0 아닌것들 재귀계속!
    # 재귀 끝나고 나오면 다시 함수 밖 반복문에서 아직 방문확인 안된 곳 중에 0이 아닌곳 탐색, or 아직 방문확인 안된 곳 중에 0이 아닌곳 있으면 다른 덩어리가 있다는 뜻이므로 다시 재귀 들어오면 바로 리턴히고 답 출력!
    dx = [0,-1,0,1]
    dy = [-1,0,1,0]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        #상하좌우중 바다0 가 있으면
        if  0 <= nx < N and 0 <= ny < M and ice_mountain[nx][ny] == 0 and visited[nx][ny] != 1:
            if ice_mountain[x][y] > 0:
                ice_mountain[x][y] -= 1
            else:
                ice_mountain[x][y] = 0
        # 상하좌우중 얼음 >0 이 있고 방문한적 없으면 재귀 들어감
        elif 0 <= nx < N and 0 <= ny < M and ice_mountain[nx][ny] > 0 and visited[nx][ny] != 1:
            visited[nx][ny] = 1
            MeltingIce(nx,ny,cnt, visited)
    

def countIce():    
    year = 0
    cnt = 0
    while cnt<2:
        cnt = 0
        visited = [[0 for col in range(M)] for row in range(N)]
        sea = 0

        for i in range(1,N-1):
            for j in range(1,M-1):
                if visited[i][j]!=1 and ice_mountain[i][j] != 0:
                    visited[i][j] = 1
                    cnt += 1
                    if cnt<2:
                        MeltingIce(i,j,cnt, visited)
                    else:
                        print(year)
                        return
                else:
                    sea += 1

        if sea == (M-2)*(N-2):
            print(0)
            return

        year += 1


#N - row num, M - col num 
N, M = [int(x) for x in stdin.readline().split()]

ice_mountain = []
for i in range(N):
    ice_mountain.append([int(x) for x in stdin.readline().split()])


countIce()