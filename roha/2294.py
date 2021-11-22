import sys 
from collections import deque

def coin_combination(coins, k):
    q = deque([(1, coin) for coin in coins])
    min_num = float('inf')
    part_sum_set = set([coin for coin in coins])
    while q:
        num, part_sum = q.popleft()
        if part_sum == k:
            min_num = min(min_num, num)
        for coin in coins:
            curr_sum = part_sum + coin
            if curr_sum >  k:
                continue
            if curr_sum not in part_sum_set:
                part_sum_set.add(curr_sum)
                q.append((num + 1, curr_sum))
    if min_num == float('inf'):
        return -1 
    return min_num

if __name__ == '__main__':
    input = sys.stdin.readline
    n, k = map(int, input().split())
    coins = sorted([int(input()) for _ in range(n)], reverse=True)
    print(coin_combination(coins, k))