import sys 
from collections import deque
def extend_one_cell(board):
    rows = len(board)
    cols = len(board[0])
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q = deque([(0, 0)])
    visited = [[False] * cols for _ in range(rows)]
    visited[0][0] = True
    while q:
        r, c = q.popleft()
        if r == rows-1 and c == cols-1:
            return True
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                visited[nr][nc] = True
                if board[nr][nc]:
                    q.append((nr, nc))
                else:
                    board[nr][nc] = 1
    return False

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    board = [list(map(int, input().rstrip())) for _ in range(n)]
    count = 0
    while not extend_one_cell(board):
        count += 1
    print(count)