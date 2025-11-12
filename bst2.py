# In bst.py, I take an iterative approach to implementing the binary search tree algorithms (insert, search, balance, etc)
# 
# Iteration means that we are using loops to repeat a set of instructions
#
# In bst2.py, I take a recursive approach to implementing the binary search tree algorithms
#
# Recursion is when a function calls itself
#
# Iteration is often preferable to recursion, because it is more efficient with respect to speed and memory
#
# There is actually some overhead to a function call
#
# When we call a function, we push a new stack frame onto the stack
#
# So if we call a recursive function a thousand times, then we push a new stack frame onto the stack a thousand times
#
# This involves a lot of I/O operations with the stack (the stack is a section of dynamic memory)
# 
# If we use iteration instead, then we can avoid a lot of unnecessary I/O operations
#
# This is why iteration is often preferable to recursion
# 
# I wanted to demonstrate both the iterative approach and the recursive approach, which is why I have two files instead of one: bst.py demonstrates the iterative approach, and bst2.py demonstrates the recursive approach
#
# Honestly, I think that bst.py is a lot more efficient
#
# We can also run into an error where the recursion limit is exceeded, when we opt for recursion
#
# One workaround is to increase the recursion limit (by means of sys.setrecursionlimit)
#
# But even if we increase the recursion limit, there is still a lot of overhead to recursive function calls
#
# So I think that bst.py is a lot more efficient, but I wanted to show both approaches
#
# I think this is a good stopping point
#
# Today is Tuesday, November 11, 2025
#
# I have some work to do, but I am also going to watch TV and take it easy
# 
# To summarize, iteration implies loops, and recursion implies that a function is calling itself
#
# Iteration and recursion are two important concepts in the study of algorithms
#
# ###### Examples ######
#
# Example #1:
#
# % cat unsorted.txt
# [7, 6, 5, 0, 8, 6, 8, 1, 6, 7]
#
# % python bst.py -i unsorted.txt -t 2
# The binary search tree has a height of 4
#
# Linear search
# --------------
# 2 is missing
# The linear search took 0.0041 milliseconds
#
# Binary search
# --------------
# 2 is missing
# The binary search took 0.0012 milliseconds
#
# Example #2:
#
# % python bst.py -n 10 2 12 4 7 8 9 20 30 4 7 5 -t 11
# Unsorted list:
#
# [10, 2, 12, 4, 7, 8, 9, 20, 30, 4, 7, 5]
#
# The binary search tree has a height of 5
#
# Linear search
# --------------
# 11 is missing
# The linear search took 0.0041 milliseconds
#
# Binary search
# --------------
# 11 is missing
# The binary search took 0.0010 milliseconds
#
# Example #3:
#
# % python bst.py -r -s 1e4 -min 0 -max 1e4 -t 1337
# The binary search tree has a height of 21
#
# Linear search
# --------------
# 1337 is present
# The linear search took 0.0830 milliseconds
#
# Binary search
# --------------
# 1337 is present
# The binary search took 0.0029 milliseconds

import random
import time
import argparse
import ast

class BinarySearchTree:
    def __init__(self, arr=None):
        self.root = None
        self.size = 0
        self.height = 0
        if arr:
            arr.sort()
            self._balance(arr, 0, len(arr) - 1)

    def _balance(self, arr, low, high):
        if low > high:
            return
        pivot_index = low + int((high - low + 1) / 2)
        pivot = arr[pivot_index]
        self.insert(pivot)
        if low < pivot_index:
            self._balance(arr, low, pivot_index - 1)
        if pivot_index < high:
            self._balance(arr, pivot_index + 1, high)

    def balance(self):
        arr = self.tolist()
        self.root = None
        self._balance(arr, 0, len(arr) - 1)

    def _insert(self, node, value):
        if value <= node.value and node.left is None:
            node.left = Node(value)
        elif value <= node.value:
            self._insert(node.left, value)
        elif value > node.value and node.right is None:
            node.right = Node(value)
        elif value > node.value:
            self._insert(node.right, value)

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _search(self, node, value):
        if value == node.value:
            return True
        elif value < node.value and node.left is None:
            return False
        elif value < node.value:
            return self._search(node.left, value)
        elif value > node.value and node.right is None:
            return False
        elif value > node.value:
            return self._search(node.right, value)

    def search(self, value):
        if self.root is None:
            return False
        return self._search(self.root, value)

    def _tolist(self, node, arr):
        if node is None:
            return
        self._tolist(node.left, arr)
        arr.append(node.value)
        self._tolist(node.right, arr)

    def tolist(self):
        arr = []
        self._tolist(self.root, arr)
        return arr

    def _calculate_height(self, node, height):
        if node is None:
            return
        height += 1
        if height > self.height:
            self.height = height
        self._calculate_height(node.left, height)
        self._calculate_height(node.right, height)

    def calculate_height(self):
        self.height = 0
        self._calculate_height(self.root, 0)
        return self.height

    def _calculate_size(self, node):
        if node is None:
            return
        self.size += 1
        self._calculate_size(node.left)
        self._calculate_size(node.right)

    def calculate_size(self):
        self.size = 0
        self._calculate_size(self.root)
        return self.size

    def str(self, node):
        if node is None:
            return ''
        elif node.left is None and node.right is None:
            return f'{node.value}'
        elif node.left and node.right is None:
            leftchild = self.str(node.left)
            return f'{node.value}({leftchild})'
        elif node.left is None and node.right:
            rightchild = self.str(node.right)
            return f'{node.value}({rightchild})'
        else:
            leftchild = self.str(node.left)
            rightchild = self.str(node.right)
            return f'{node.value}({leftchild})({rightchild})'

    def __str__(self):
        size = self.calculate_size()
        if size <= 100:
            return self.str(self.root)
        height = self.calculate_height()
        return f'Size: {size} Height: {height}'

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='bst2.py', description='Binary search')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-i', '--inputfile', type=str)
    group.add_argument('-n', '--numbers', nargs='+', type=int) 
    group.add_argument('-r', '--random', action='store_true')
    parser.add_argument('-s', '--size', type=float, default=10)
    parser.add_argument('-min', '--minimum', type=float, default=0)
    parser.add_argument('-max', '--maximum', type=float, default=100)
    parser.add_argument('-t', '--test', nargs='+', type=int)
    args = parser.parse_args()
    if args.inputfile:
        with open(args.inputfile, 'r') as file:
            contents = file.read()
            arr = ast.literal_eval(contents)
    elif args.numbers:
        arr = args.numbers
    elif args.random:
        size, min, max = int(args.size), int(args.minimum), int(args.maximum)
        arr = [random.randint(min, max) for i in range(size)]
    tree = BinarySearchTree(arr)
    if len(arr) < 1000:
        print(f'Unsorted list')
        print('------------------------------')
        print(f'{arr}\n')
    size = tree.calculate_size()
    height = tree.calculate_height()
    print('Statistics')
    print('------------------------------')
    print(f'The binary search tree has a size of {size} and a height of {height}\n')
    print('String representation')
    print('------------------------------')
    print(tree)
    if args.test:
        print('')
        print('Linear search results')
        print('------------------------------')
        for i in range(len(args.test)):
            value = args.test[i]
            start_time = time.time()
            found = False
            for j in range(len(arr)):
                if value == arr[j]:
                    found = True
                    break
            time_elapsed = 1000 * (time.time() - start_time)
            print(f'{value} is present' if found else f'{value} is missing')
            print(f'The linear search took {time_elapsed:.4f} milliseconds')
            if i < len(args.test) - 1:
                print('')
        print('')
        print('Binary search results')
        print('------------------------------')
        for i in range(len(args.test)):
            value = args.test[i]
            start_time = time.time()
            found = tree.search(value)
            time_elapsed = 1000 * (time.time() - start_time)
            print(f'{value} is present' if found else f'{value} is missing')
            print(f'The binary search took {time_elapsed:.4f} milliseconds')
            if i < len(args.test) - 1:
                print('')
