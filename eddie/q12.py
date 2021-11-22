import collections
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

bigger = collections.defaultdict(list)
smaller = collections.defaultdict(list)

N, M = map(int, input().split())

for _ in range(M):
    u, v = map(int, input().split())
    smaller[u].append(v)
    bigger[v].append(u)


def check_smaller(bead):
    global count, visited

    visited[bead] = 1

    if smaller[bead]:
        nexts = smaller[bead]

        for next in nexts:
            if visited[next] == 0:
                count += 1
                check_smaller(next)


def check_bigger(bead):
    global count, visited

    visited[bead] = 1

    if bigger[bead]:
        nexts = bigger[bead]

        for next in nexts:
            if visited[next] == 0:
                count += 1
                check_bigger(next)

ans = 0

for bead in list(smaller):
    count = 0
    visited = [0] * (N + 1)
    check_smaller(bead)
    if count > (N - 1) // 2:
        ans += 1

for bead in list(bigger):
    count = 0
    visited = [0] * (N + 1)
    check_bigger(bead)
    if count > (N - 1) // 2:
        ans += 1

print(ans)