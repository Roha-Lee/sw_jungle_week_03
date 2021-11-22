# 11	2573	상	DFS	빙산
from sys import stdin, setrecursionlimit
setrecursionlimit(10**8)
def MeltingIce(x, y, visited):
    visited[x][y] = 1
    dx = [0,-1,0,1]
    dy = [-1,0,1,0]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] != 1:
            if ice_mountain[nx][ny] == 0:
                ice_mountain[x][y] = max(0, ice_mountain[x][y]-1)       
            elif ice_mountain[nx][ny] > 0:
                MeltingIce(nx, ny, visited)      
def countIce():    
    year = 0
    while True:
        cnt = 0
        visited = [[0 for col in range(M)] for row in range(N)]
        for i in range(1,N-1):
            for j in range(1,M-1):
                if visited[i][j]!=1 and ice_mountain[i][j] != 0:
                    cnt +=1
                    MeltingIce(i, j, visited)
        if cnt>=2:
            print(year)
            return        
        elif cnt == 0:
            print(0)
            return
        year += 1

if __name__ == '__main__':
    N, M = [int(x) for x in stdin.readline().split()]
    ice_mountain = [list(map(int, stdin.readline().split())) for _ in range(N)]
    countIce()