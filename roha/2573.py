import sys 
def melt_down_1_year(worlds):
    rows = len(worlds)
    cols = len(worlds[0])
    visited = [[False] * cols for _ in range(rows)]
    count = 0
    for r in range(1, rows-1):
        for c in range(1, cols-1):
            if worlds[r][c] > 0 and not visited[r][c]:
                count += 1
                _melt(worlds, r, c, visited)
    return count
    

def _melt(worlds, r, c, visited):
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    rows = len(worlds)
    cols = len(worlds[0])
    visited[r][c] = True
    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and worlds[nr][nc] == 0 and not visited[nr][nc]:
            worlds[r][c] = max(0, worlds[r][c] - 1)
    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and worlds[nr][nc] and not visited[nr][nc]:
            _melt(worlds, nr, nc, visited)
    
            
if __name__ == '__main__':
    sys.setrecursionlimit(10**8)
    input = sys.stdin.readline
    rows, cols = map(int, input().split())
    worlds = [list(map(int, input().split())) for _ in range(rows)]
    years = -1
    while True:
        num_parts = melt_down_1_year(worlds)
        years += 1

        if num_parts > 1:
            break
        if num_parts == 0:
            years = 0
            break

    print(years)