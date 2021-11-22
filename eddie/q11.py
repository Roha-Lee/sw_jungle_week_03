import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

rows, cols = map(int, input().split())

board = []
for _ in range(rows):
    row = list(map(int, input().split()))
    board.append(row)


def dfs(row, col):
    if visited[row][col] == 1:
        return

    visited[row][col] = 1

    nexts = []
    nexts.append([row, col + 1, board[row][col + 1]])
    nexts.append([row, col - 1, board[row][col - 1]])
    nexts.append([row + 1, col, board[row + 1][col]])
    nexts.append([row - 1, col, board[row - 1][col]])

    for next in nexts:
        if next[2] == 0 and visited[next[0]][next[1]] == 0:
            if board[row][col] > 0:
                board[row][col] -= 1
        else:
            dfs(next[0], next[1])

year = 0

while True:
    year += 1

    # Initialize visited for each year
    visited = []
    for i in range(rows):
        tmp = []
        for j in range(cols):
            tmp.append(0)
        visited.append(tmp)

    # run dfs on first non-zero block
    for row in range(rows):
        for col in range(cols):
            if board[row][col] > 0:
                dfs(row, col)
                break
        else:
            continue
        break
    else: # print 0 and exit if all ice has melted
        print(0)
        sys.exit(0)

    for row in range(rows):
        for col in range(cols):
            if visited[row][col] == 0 and board[row][col] > 0: # exit if any block is non-zero but not visited
                print(year - 1)
                sys.exit(0)

