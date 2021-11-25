### Solution using dictionary
import sys

N = int(sys.stdin.readline())
tree = {}

for _ in range(N):
    root, left, right = sys.stdin.readline().split()
    tree[root] = [left, right]

def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])

def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])

def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')


### Solution using class
# class Node:

#     def __init__(self, value):
#         self.left  = None
#         self.right = None
#         self.value = value

# class Tree:

#     def __init__(self, root, left, right):
#         self.root = Node(root)
#         if left != '.':
#             self.root.left = Node(left)
#         if right != '.':
#             self.root.right = Node(right)
#         self.current = self.root

#     def append(self, parent, left, right):
#         self.current = self.root
#         stack = []
#         if self.current.right:
#             stack.append(self.current.right)
#         if self.current.left:
#             stack.append(self.current.left)
#         while stack:
#             self.current = stack.pop()
#             if self.current.value == parent:
#                 if left != '.':
#                     self.current.left = Node(left)
#                 if right != '.':
#                     self.current.right = Node(right)
#                 return

#             if self.current.right:
#                 stack.append(self.current.right)
#             if self.current.left:
#                 stack.append(self.current.left)

#     def print_tree(self, traversal_type):
#         if traversal_type == 'preorder':
#             return self.preorder_print(tree.root, '')
#         elif traversal_type == 'inorder':
#             return self.inorder_print(tree.root, '')
#         elif traversal_type == 'postorder':
#             return self.postorder_print(tree.root, '')

#     def preorder_print(self, start, traversal):
#         if start:
#             traversal += str(start.value)
#             traversal = self.preorder_print(start.left, traversal)
#             traversal = self.preorder_print(start.right, traversal)
#         return traversal

#     def inorder_print(self, start, traversal):
#         if start:
#             traversal = self.inorder_print(start.left, traversal)
#             traversal += str(start.value)
#             traversal = self.inorder_print(start.right, traversal)
#         return traversal

#     def postorder_print(self, start, traversal):
#         if start:
#             traversal = self.postorder_print(start.left, traversal)
#             traversal = self.postorder_print(start.right, traversal)
#             traversal += str(start.value)
#         return traversal


# N = int(input())
# root, left, right = input().split()
# tree = Tree(root, left, right)
# for _ in range(N - 1):
#     parent, left, right = input().split()
#     tree.append(parent, left, right)


# print(tree.print_tree('preorder'))
# print(tree.print_tree('inorder'))
# print(tree.print_tree('postorder'))
