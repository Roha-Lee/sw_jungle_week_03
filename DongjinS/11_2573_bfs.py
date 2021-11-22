# 11	2573	상	DFS x! BFS	빙산
# BFS 풀고 다시 풀기..
from sys import stdin, setrecursionlimit
setrecursionlimit(10**8)

N, M = [int(x) for x in stdin.readline().split()]
ice_mountain = [list(map(int, stdin.readline().split())) for _ in range(N)]
