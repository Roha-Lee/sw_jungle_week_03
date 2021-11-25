import sys 
from collections import deque

def escape_maze(board):
    rows = len(board)
    cols = len(board[0])
    visited = [[False] * cols for _ in range(rows)]
    visited[0][0] = True
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q = deque([(0,0)])
    
    step = 0
    while q:
        curr_steps = deque()
        while q:
            curr_steps.append(q.popleft())
        step += 1
        while curr_steps:
            r, c = curr_steps.popleft()
            if r == rows-1 and c == cols-1:
                return step
            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and board[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr, nc))
        

if __name__ == '__main__':
    input = sys.stdin.readline
    n, m = map(int, input().split())
    board = [list(map(int, input().rstrip())) for _ in range(n)]
    print(escape_maze(board))

