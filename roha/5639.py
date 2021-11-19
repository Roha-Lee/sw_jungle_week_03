
import sys 
sys.setrecursionlimit(10000000)

# 재귀 구현 
def pre_to_post(nums):
    length = len(nums)
    
    if length <= 1:
        return nums

    for i in range(1, length):
        if nums[i] > nums[0]:
            return pre_to_post(nums[1:i]) + pre_to_post(nums[i:]) + [nums[0]]

    return pre_to_post(nums[1:]) + [nums[0]]
    

if __name__ == '__main__':
    input = sys.stdin.readline
    preorder_result = []
    while True:
        usr_input = input().rstrip()
        if usr_input == '':
            break
        preorder_result.append(int(usr_input))
    print(*pre_to_post(preorder_result), sep='\n')


# import sys 
# def pre_to_in(pre):
#     result = []
#     stack = []
    
#     for num in pre:
#         while stack and stack[-1] < num:
#             result.append(stack.pop())
#         stack.append(num)
#     while stack:
#         result.append(stack.pop())
#     return result

# # 스택 구현 미완성
# def pre_to_post_(pre):
#     result = []
#     left_child = [pre[0]]
#     right_child = []
    
#     for num in pre[1:]:
#         if left_child[-1] < num:
#             while right_child and right_child[-1] < num:
#                 result.append(right_child.pop())
#             right_child.append(num)
#         else:
#             left_child.append(num)
        
#         while   right_child and \
#                 len(left_child) > 1 and \
#                 left_child[-1] < right_child[-1] and \
#                 left_child[-2] < right_child[-1]:
#             result.append(left_child.pop())    
    
#     return result