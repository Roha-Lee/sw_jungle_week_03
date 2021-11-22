import collections
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

N = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))

max = -float('inf')
min = float('inf')

def dfs(num, count):
    global max, min

    if count == len(nums) - 1:
        if num > max:
            max = num
        if num < min:
            min = num
        return

    count += 1

    if operators[0] > 0:
        operators[0] -= 1
        dfs(num + nums[count], count)
        operators[0] += 1
    if operators[1] > 0:
        operators[1] -= 1
        dfs(num - nums[count], count)
        operators[1] += 1
    if operators[2] > 0:
        operators[2] -= 1
        dfs(num * nums[count], count)
        operators[2] += 1
    if operators[3] > 0:
        operators[3] -= 1
        if num < 0:
            dfs(-1 * (-num // nums[count]), count)
        else:
            dfs(num // nums[count], count)
        operators[3] +=1

dfs(nums[0], 0)
print(max)
print(min)


