# ###### Introduction ######
#
# Binary search trees teach us a lot about algorithms and data structures
#
# What is an algorithm? What is a data structure?
#
# In my opinion an algorithm is a list of instructions
#
# In my opinion a data structure is a way of structuring data
#
# We can structure data in a way that meets our needs
#
# If we want to reduce search time, we can use a hash map or a binary search tree
#
# If there is no need to reduce search time, we can use an array or a list, because they require less memory
#
# If we want to process events in a first-in first-out manner, we can use a queue
#
# If we want to process events in a last-in first-out manner, we can use a stack
#
# It is helpful to know some common data structures
#
# Below is a list of some common data structures
#
# 1. Arrays
# 2. Lists (e.g. array lists, linked lists, Python lists)
# 3. Stacks
# 4. Queues
# 5. Maps (e.g. hash maps, Python dictionaries)
# 6. Trees (e.g. binary search trees, B-trees)
# 7. Graphs
#
# Now, let's return to the original topic, the topic of binary search trees
#
# How do binary search trees fit in? What are some applications of binary search trees?
#
# As we said before, binary search trees can be used to reduce search time
#
# We can actually use a binary search tree to index a database table (like a relational database table)
#
# Instead of doing a linear search through a list of records, which has a time complexity of O(n), we can do a binary search through a tree of records, which has a time complexity of O(log n)
#
# This is a much more efficient way of searching a database table for a specific record, or for a set of records that share a certain key (the key could be a customer ID or a customer's full name)
#
# When we create a binary search tree from a table of records for a given key, we use the key to organize the tree, order the nodes, and assign each record to a node
#
# When two records share the same key, they get assigned to the same node, and they get chained as a linked list
#
# The chaining principle also applies to hash maps
#
# In hash maps, when two keys translate to the same array index, the values get stored at the same array index as a linked list
#
# In binary search trees, when two records have the same key, the records get stored in the same node as a linked list
#
# So, for example, if a binary search tree uses name as its key, and two customers have the same name, then their customer records get chained together as a linked list and stored in the same node
#
# I wanted to make the chaining principle clear
#
# I also wanted to make it clear how a binary search tree is created out of a table of records for a given key
#
# When we index a relational database table, the indexed columns become the key in a binary search tree
#
# Now, we have spent a long time talking about binary search trees and how they are structured
#
# Let's talk about the binary search tree algorithms
#
# The binary search tree algorithms are well suited to recursion
#
# You may have heard the words "recursion" and "iteration" used when talking about algorithms
#
# What is recursion? What is iteration?
#
# Recursion means that a function is calling itself
#
# Iteration means that we are using a loop to repeat a set of instructions
#
# So, recursion implies that a function is calling itself
#
# Iteration implies loops
#
# It is possible to write the insert, search, and balance methods using iteration
#
# But is easier and more elegant to write these methods using recursion
#
# The quicksort.py file makes ample use of recursion, and so does the bst.py file
#
# There are arguments and counterarguments to using recursion
#
# One argument for recursion is that it is often simpler and more elegant than iteration
#
# A counterargument is that recursion involves some overhead
#
# Every function call has some overhead
#
# When we call a function, we push a new stack frame onto the stack
#
# When we return from a function, we pop a stack frame from the stack
#
# If we make a thousand recursive function calls, the stack I/O adds up, and it adds some overhead to our program
#
# But we can minimize the number of recursive function calls, by balancing our binary search tree
#
# Honestly, I think that the recursive implementation is so elegant that it is worth the small amount of overhead
#
# Also, some algorithms are difficult to write in an iterative manner
#
# I can write the insert, search, and balance methods using iteration
#
# But I do not know how to write the str and tolist methods using iteration
#
# So, I think this is a good stopping point
#
# In these comments we talked about the following subjects: algorithms, data structures, recursion, and iteration
#
# Let us quickly summarize by defining these words
#
# An algorithm is a list of instructions
#
# A data structure is a way of structuring data
#
# Recursion is a technique in which a function calls itself
#
# Iteration is a technique in which a loop is used to repeat a set of instructions
#
# Binary search trees teach us a lot about algorithms and data structures
#
# A binary search tree is a data structure that can be used to reduce search time
#
# Its algorithms are well suited to recursion
#
# Today is Sunday, November 16, 2025
#
# This series of comments has undergone many revisions
#
# But each time, I am able to improve it
#
# I have some work to do, and I am also going to watch TV and relax
#
# I wish everyone a nice week
#
# Andrew
#
# ###### Examples ######
#
# Example 1: Create a binary search tree out of a list of elements
#
# % python bst.py -n 0 1 2 3 4 5 6 7 8 9
# Unsorted list
# ------------------------------
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# Statistics
# ------------------------------
# Root value: 4 Node count: 10 Value count: 10 Height: 4
#
# String representation
# ------------------------------
# 4(1(0)(2(3)))(7(5(6))(8(9)))
#
# Example 2: Create a binary search tree out of a randomly generated list of elements
#
# % python bst.py -r -s 10 -min 0 -max 10
# Unsorted list
# ------------------------------
# [8, 5, 0, 7, 6, 0, 6, 7, 5, 4]
#
# Statistics
# ------------------------------
# Root value: 5 Node count: 6 Value count: 10 Height: 3
#
# String representation
# ------------------------------
# 5(0(4))(7(6)(8))
#
# Example 3: Create a binary search tree from an input file and search the tree for a given value
#
# % cat unsorted.txt
# [5, 3, 2, 1, 4]
#
# % python bst.py -i unsorted.txt -t 3
# Unsorted list
# ------------------------------
# [5, 3, 2, 1, 4]
#
# Statistics
# ------------------------------
# Root value: 3 Node count: 5 Value count: 5 Height: 3
#
# String representation
# ------------------------------
# 3(1(2))(4(5))
#
# Linear search results
# ------------------------------
# 3 is present
# The linear search took 0.0010 milliseconds
#
# Binary search results
# ------------------------------
# 3 is present
# The binary search took 0.0007 milliseconds
#
# Example 4: Create a binary search tree from an input file and write its string representation to an output file
#
# % cat unsorted.txt
# [5, 3, 2, 1, 4]
#
# % python bst.py -i unsorted.txt -o tree.txt
# Unsorted list
# ------------------------------
# [5, 3, 2, 1, 4]
#
# Statistics
# ------------------------------
# Root value: 3 Node count: 5 Value count: 5 Height: 3
#
# String representation
# ------------------------------
# 3(1(2))(4(5))
#
# % cat tree.txt
# 3(1(2))(4(5))

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

    def find_min_node(self, node):
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
            successor = self.find_min_node(node.right)
            node.value = successor.value
            node.right = self._delete(node.right, successor.value)
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
