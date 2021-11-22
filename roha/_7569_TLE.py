import sys 
from copy import deepcopy
from collections import deque
def ripe_tomato(tomatos, visited, h, r, c):
    heights = len(tomatos)
    rows = len(tomatos[0])
    cols = len(tomatos[0][0])
    tomatos = deepcopy(tomatos)
    moves = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    q = deque([(h, r, c)])
    visited[h][r][c] = True

    while q:
        h, r, c = q.popleft()
        for dh, dr, dc in moves:
            nh, nr, nc = h + dh, r + dr, c + dc
            if  0 <= nh < heights and 0 <= nr < rows and 0 <= nc < cols and not visited[nh][nr][nc]:
                visited[nh][nr][nc] = True
                if tomatos[nh][nr][nc] == 0:
                    tomatos[nh][nr][nc] = 1
                elif tomatos[nh][nr][nc] == 1:
                    q.append((nh, nr, nc))
    return tomatos

def is_changed_and_ripen(before, after):
    heights = len(before)
    rows = len(before[0])
    cols = len(before[0][0])
    changed = False
    ripen = True
    for h in range(heights):
        for r in range(rows):
            for c in range(cols):
                if before[h][r][c] != after[h][r][c]:
                    changed = True
                if after[h][r][c] == 0:
                    ripen = False
    return changed, ripen

def check_tomatos(tomatos, h, n, m):
    days = 0
    while True:
        visited = [[[False] * m for _ in range(n)] for _ in range(h)]
        days += 1
        for height in range(h):
            for row in range(n):
                for col in range(m):
                    if tomatos[height][row][col] == 1 and not visited[height][row][col]:
                        after_tomatos = ripe_tomato(tomatos, visited, height, row, col)
        changed, ripen = is_changed_and_ripen(tomatos, after_tomatos)
        tomatos = after_tomatos
        if not changed and not ripen:
            return -1
        elif not changed and ripen:
            return days - 1
                        
if __name__ == '__main__':
    input = sys.stdin.readline
    m, n, h = map(int, input().split())
    tomatos = []
    for _ in range(h):
        tomatos.append([list(map(int, input().split())) for _ in range(n)])
    print(check_tomatos(tomatos, h, n, m))