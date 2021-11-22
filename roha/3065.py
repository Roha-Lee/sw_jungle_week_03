import sys 
from collections import deque

def escape(board, hedgehog_locs, water_locs):
    rows = len(board)
    cols = len(board[0])
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [[False] * cols for _ in range(rows)]

    for r, c in water_locs + hedgehog_locs:
        visited[r][c] = True
    
    time = 0
    while hedgehog_locs:
        time += 1
        curr_hedgehog_locs = deque()
        while hedgehog_locs:
            curr_hedgehog_locs.append(hedgehog_locs.popleft())
        while curr_hedgehog_locs:
            r, c = curr_hedgehog_locs.popleft()
            if board[r][c] == 2:
                continue
            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                    visited[nr][nc] = True
                    if board[nr][nc] == 3:
                        hedgehog_locs.append((nr, nc))
                    if board[nr][nc] == 0:
                        return time
            
        curr_water_locs = deque()
        while water_locs:
            curr_water_locs.append(water_locs.popleft())
        
        while curr_water_locs:
            r, c = curr_water_locs.popleft()
            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if board[nr][nc] == 3:
                        board[nr][nc] = 2
                        water_locs.append((nr, nc))
    return 'KAKTUS'

def letter_to_digit(letter):
    map_dict = {'D': 0, 'S': 1, '*': 2, '.': 3, 'X': 4}
    return map_dict[letter]

if __name__ == '__main__':
    input = sys.stdin.readline
    rows, cols = map(int, input().split())
    board = [[0] * cols for _ in range(rows)]
    hedgehog_locs = deque()
    water_locs = deque()
    for r in range(rows):
        one_row = list(map(letter_to_digit, input().rstrip()))
        for c in range(cols):
            board[r][c] = one_row[c]
            if one_row[c] == 1:
                hedgehog_locs.append((r, c))
            elif one_row[c] == 2:
                water_locs.append((r, c))
    print(escape(board, hedgehog_locs, water_locs))


