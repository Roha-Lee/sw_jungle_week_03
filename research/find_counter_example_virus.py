from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)

def find(target):
    if parent[target] == target:
        return target
    else:
        parent[target] = find(parent[target])
        return parent[target]

def union(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    elif x<y:
        parent[y] = x
    else:
        parent[x] = y

com_n = int(stdin.readline())
connect_n = int(stdin.readline())

com_pair = []
for i in range(connect_n):
    c1,c2 = [int(x) for x in stdin.readline().split()]
    com_pair.append([c1,c2])
    com_pair.append([c2,c1])

com_pair.sort()
parent = list(range(com_n+1))

for c1, c2 in com_pair:
    if find(c1) != find(c2):
        union(c1,c2)
print(com_pair)
print(parent)
ans = 0
for i in parent:
    if i == 1:
        ans+=1
print(ans-1)