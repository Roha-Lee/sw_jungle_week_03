# 1	1991	하	그래프 탐색 기본	트리 순회	9-1
from sys import stdin

def PreOrder(root:str):
    #시작점 찾기 - 전위는 항상 A부터
    if root !=".":
        pre_ans.append(root)
        PreOrder(bi_tree[root][0])
        PreOrder(bi_tree[root][1])

    return

def InOrder(root: str):
    if root != ".":
        InOrder(bi_tree[root][0])
        in_ans.append(root)
        InOrder(bi_tree[root][1])

    return

def PostOrder(root: str):
    if root !=".":
        PostOrder(bi_tree[root][0])
        PostOrder(bi_tree[root][1])
        post_ans.append(root)

    return

n = int(stdin.readline())

bi_tree = {}
for _ in range(n):
    tmp_tree = [x for x in stdin.readline().split()]
    bi_tree[tmp_tree[0]] = [tmp_tree[1],tmp_tree[2]]

pre_ans = []
in_ans = []
post_ans = []

PreOrder("A")
print("".join(pre_ans))

InOrder("A")
print("".join(in_ans))

PostOrder("A")
print("".join(post_ans))