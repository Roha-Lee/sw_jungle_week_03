import sys 
from collections import deque
from copy import deepcopy
def get_max_days(results, heights, rows, cols):
    max_days = 0
    for h in range(heights):
        for r in range(rows):
            for c in range(cols):
                if results[h][r][c] == 0:
                    return -1
                else:
                    max_days = max(max_days, results[h][r][c])
    return max_days - 1


def find_ripe_tomatos(tomatos, heights, rows, cols, visited):
    q = deque()
    for h in range(heights):
        for r in range(rows):
            for c in range(cols):
                if tomatos[h][r][c] == 1:
                    q.append((h, r, c))
                    visited[h][r][c] = True
    return q


def check_tomatos(tomatos):
    heights = len(tomatos)
    rows = len(tomatos[0])
    cols = len(tomatos[0][0])
    tomatos = deepcopy(tomatos)
    
    visited = [[[False] * cols for _ in range(rows)] for _ in range(heights)]
    moves = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    q = find_ripe_tomatos(tomatos, heights, rows, cols, visited)
    while q:
        h, r, c = q.popleft()
        for dh, dr, dc in moves:
            nh, nr, nc = h + dh, r + dr, c + dc
            if  0 <= nh < heights and 0 <= nr < rows and 0 <= nc < cols and \
                not visited[nh][nr][nc] and not tomatos[nh][nr][nc] == -1:
                
                visited[nh][nr][nc] = True
                q.append((nh, nr, nc))
                tomatos[nh][nr][nc] = tomatos[h][r][c] + 1
    
    return get_max_days(tomatos, heights, rows, cols)

if __name__ == '__main__':
    input = sys.stdin.readline
    m, n, h = map(int, input().split())
    tomatos = []
    for _ in range(h):
        tomatos.append([list(map(int, input().split())) for _ in range(n)])
    print(check_tomatos(tomatos))