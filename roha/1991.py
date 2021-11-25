import sys 

def preorder(tree, node = 'A', result = []):
    if node == '.':
        return 
    
    result.append(node)
    preorder(tree, tree[node][0], result)
    preorder(tree, tree[node][1], result)
    return result


def inorder(tree, node = 'A', result = []):
    if node == '.':
        return 
    
    inorder(tree, tree[node][0], result)
    result.append(node)
    inorder(tree, tree[node][1], result)
    return result

def postorder(tree, node = 'A', result = []):
    if node == '.':
        return 
        
    postorder(tree, tree[node][0], result)
    postorder(tree, tree[node][1], result)
    result.append(node)
    return result


if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    tree = dict()

    for i in range(n):
        val, lc, rc = input().split()        
        tree[val] = (lc, rc)

    print(*preorder(tree, 'A'), sep='')
    print(*inorder(tree, 'A'), sep='')
    print(*postorder(tree, 'A'), sep='')    
    
        