# 2	5639	하	그래프 탐색 기본	이진 검색 트리	9-2
'''
이진 검색 트리는 다음과 같은 세 가지 조건을 만족하는 이진 트리이다.

노드의 왼쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 작다.
노드의 오른쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 크다.
왼쪽, 오른쪽 서브트리도 이진 검색 트리이다.

이진 검색 트리를 전위 순회한 결과가 주어졌을 때, 이 트리를 후위 순회한 결과를 구하는 프로그램을 작성하시오.
'''
from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)

pre_res = []
while True:
    node = (stdin.readline())
    if node == "" or not node.isnumeric or node == "\n":
        break
    pre_res.append(int(node))

# print(pre_res)
post_order = []
def MakePostOrder(pre_res:list, start: int, end: int):
    if start>end:
        return

    root = pre_res[start]

    ls = start + 1
    re = end
    rs = end + 1
    repeat = end-start+1
    for i in range(1,repeat):
        now = pre_res[start + i] 
        if now > root:
            rs = start + i
            break

    le = rs - 1
    MakePostOrder(pre_res, ls, le)
    MakePostOrder(pre_res, rs, re)
    
    post_order.append(root)

MakePostOrder(pre_res, 0, len(pre_res)-1)
for a in post_order:
    print(a)
