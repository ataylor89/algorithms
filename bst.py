# In bst.py, I take a recursive approach, whereas in bst2.py, I take an iterative approach
#
# Recursion means that a function is calling itself
#
# Iteration means that a loop is being used to repeat a set of instructions
#
# So recursion implies that a function is calling itself
#
# Iteration implies loops
#
# It is often the case that iteration is more efficient than recursion, because there is an overhead to each function call
# (Every time we call a function, we push a new stack frame onto the stack)
#
# On the other hand, recursion is often easier, simpler, and more elegant than iteration
#
# So there's a tradeoff...
#
# Recursion can be easier to implement, but iteration can be more efficient with respect to speed and memory
#
# I wanted to show both approaches to creating a binary search tree (the recursive approach and the iterative approach)
#
# It's also a good opportunity to learn about recursion and iteration
#
# Recursion and iteration are important tools in algorithm design
#
# I mentioned the stack earlier
#
# You might be wondering, "What is the stack?"
#
# When a process gets started, the operating system gives it its own virtual address space
#
# The virtual address space includes a stack, a heap, a code segment, and a data segment
#
# The stack is a convenient structure for storing data
#
# From an assembly perspective, two of the most convenient ways of storing data are...
# 1) Registers
# 2) The stack
#
# We can also allocate memory on the heap, but that takes more time than pushing data onto the stack
# 
# So, to return to the original point I was making, about recursion...
#
# Every time we call a function, we push data onto the stack
#
# The data that we push depends on the CPU architecture, but...
#
# We often push a function's arguments, local variables, and return address onto the stack
#
# Also, we sometimes push callee-saved registers onto the stack
#
# This means that there is overhead to every function call
#
# With each function call, we have to perform many I/O operations on the stack
#
# When a function returns, we have to perform more I/O operations, because we pop data from the stack to return it to the way it used to be before the function was called
#
# I wanted to point out that there is overhead to each function call, and explain what this overhead consists of
#
# Because of the overhead associated with each function call, iteration is often more efficient than recursion
#
# But, as I said before, there is a tradeoff
#
# Iteration is often more efficient, but recursion is often easier to implement
#
# I think it's really useful to know both approaches: iteration and recursion
#
# If you consider our quicksort algorithm in quicksort.py, you'll notice that it is a lot easier to write this algorithm in a recursive way than it is to write this algorithm in an iterative way
#
# In fact, I do not know an iterative way of writing the quicksort algorithm
#
# (I only know the recursive implementation)
#
# There's a big question in computer science: can every recursive algorithm be turned into an iterative algorithm?
#
# If the answer to this question is yes, then it is true in theory, but it is still difficult in practice
#
# A lot of tasks are made easier by recursion, so I think it's really useful to know both iteration and recursion
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
        self.node_count = 0
        self.value_count = 0
        self.height = 0
        if arr:
            arr.sort()
            self._balance(arr, 0, len(arr) - 1)

    def _balance(self, arr, start, end):
        if start > end:
            return
        mid = (start + end) // 2
        self.insert(arr[mid])
        self._balance(arr, start, mid - 1)
        self._balance(arr, mid + 1, end)

    def balance(self):
        arr = self.tolist()
        self.root = None
        self.node_count = 0
        self.value_count = 0
        self.height = 0
        self._balance(arr, 0, len(arr) - 1)

    def _insert(self, node, value):
        if node is None:
            node = Node(value)
        elif value == node.value:
            node.frequency += 1
        elif value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)
        return node

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _search(self, node, value):
        if node is None:
            return False
        elif value == node.value:
            return True
        elif value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)

    def search(self, value):
        return self._search(self.root, value)

    def get_successor(self, node):
        node = node.right
        while node is not None and node.left is not None:
            node = node.left
        return node

    def _delete(self, node, value):
        if node is None:
            return None
        elif value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            succ = self.get_successor(node)
            node.value = succ.value
            node.right = self._delete(node.right, succ.value)
        return node

    def delete(self, value):
        self.root = self._delete(self.root, value)

    # We perform an inorder traversal to get a list of values in increasing order
    def _tolist(self, node, arr):
        if node is None:
            return
        self._tolist(node.left, arr)
        for i in range(node.frequency):
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
        self.node_count += 1
        self.value_count += node.frequency
        self._calculate_size(node.left)
        self._calculate_size(node.right)

    def calculate_size(self):
        self.node_count = 0
        self.value_count = 0
        self._calculate_size(self.root)
        return (self.node_count, self.value_count)

    # We perform a preorder traversal to get a string representation of the binary search tree
    def _str(self, node):
        if node is None:
            return ''
        elif node.left is None and node.right is None:
            return f'{node.value}'
        elif node.left and node.right is None:
            leftchild = self._str(node.left)
            return f'{node.value}({leftchild})'
        elif node.left is None and node.right:
            rightchild = self._str(node.right)
            return f'{node.value}({rightchild})'
        else:
            leftchild = self._str(node.left)
            rightchild = self._str(node.right)
            return f'{node.value}({leftchild})({rightchild})'

    def str(self):
        return self._str(self.root)

    def __str__(self):
        return self.str()

    def stats(self):
        root_value = self.root.value if self.root else None
        node_count, value_count = self.calculate_size()
        height = self.calculate_height()
        return f'Root value: {root_value} Node count: {node_count} Value count: {value_count} Height: {height}'

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.frequency = 1

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
    parser.add_argument('-o', '--outputfile', type=str)
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
    if len(arr) <= 1000:
        print(f'Unsorted list')
        print('------------------------------')
        print(f'{arr}\n')
    tree = BinarySearchTree(arr)
    print('Statistics')
    print('------------------------------')
    print(tree.stats())
    prefix_expression = tree.str()
    if tree.node_count <= 1000:
        print('')
        print('String representation')
        print('------------------------------')
        print(prefix_expression)
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
    if args.outputfile:
        with open(args.outputfile, 'w') as file:
            file.write(prefix_expression)
