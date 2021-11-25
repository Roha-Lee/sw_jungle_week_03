import sys 
from collections import defaultdict, deque
def find_total_part_nums(n, graph, inward_count):
    part_nums = {i:0 for i in range(1, n+1)}
    q = deque()
    for key, value in inward_count.items():
        if value == 0:
            q.append(key)
    
    while q:
        part = q.popleft()
        for cost, neighbor in graph[part]:
            val = 1 if part_nums[part] == 0 else part_nums[part]
            part_nums[neighbor] += val * cost 
            inward_count[neighbor] -= 1
            if inward_count[neighbor] == 0:
                q.append(neighbor)
    
    result = []
    for part, nums in part_nums.items():
        if len(graph[part]) == 0:
            result.append((part, nums))
    return sorted(result)


if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    
    graph = defaultdict(list)
    inward_count = {i:0 for i in range(1, n+1)}
    

    for _ in range(m):
        src, dst, cost = map(int, input().split())
        graph[src].append((cost, dst))
        inward_count[dst] += 1
    
    for part, num in find_total_part_nums(n, graph, inward_count):
        print(part, num)