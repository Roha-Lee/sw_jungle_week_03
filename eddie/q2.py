import sys

sys.setrecursionlimit(10 ** 9)

def post_order(start, end):
    if start > end:
        return

    root = pre_order[start]
    idx = start + 1

    # find index where value is greater than root
    while idx <= end:
        if pre_order[idx] > root:
            break
        idx += 1

    # call recursion on left subtree
    post_order(start + 1, idx - 1)

    # call recursion on right subtree
    post_order(idx, end)

    print(root)

pre_order = []

while True:
    try:
        pre_order.append(int(input()))
    except:
        break

post_order(0, len(pre_order) - 1)