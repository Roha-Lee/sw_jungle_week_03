import sys 
from operator import add, sub, mul
from itertools import permutations
def div(num1, num2):
    return int(num1 / num2)

def calc_curr(result, new_num, op_idx):
    op_dict = {
        0: add,
        1: sub,
        2: mul, 
        3: div
    }
    operation = op_dict[op_idx]
    return operation(result, new_num)

def find_max_min_result(arr, curr, operator_nums, part_sum):
    global min_val, max_val
    if curr == len(arr):
        min_val = min(part_sum, min_val)
        max_val = max(part_sum, max_val)
        return 
    
    for op_idx in range(4):
        if operator_nums[op_idx]:
            operator_nums[op_idx] -= 1
            find_max_min_result(arr, 
                                curr+1, 
                                operator_nums, 
                                calc_curr(part_sum, arr[curr], op_idx))
            operator_nums[op_idx] += 1

    
if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    arr = list(map(int, input().split()))
    operator_nums = list(map(int, input().split()))
    min_val, max_val = float('inf'), -float('inf')
    find_max_min_result(arr, 1, operator_nums, arr[0])
    print(max_val)
    print(min_val)
    