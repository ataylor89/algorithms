# ###### Introduction ######
#
# Binary search trees teach us a lot about algorithms and data structures
#
# What is an algorithm? What is a data structure?
#
# In my opinion an algorithm is a list of instructions
#
# In my opinion a data structure is a database
#
# We have many synonyms for the word "database"
#
# The word "table" is synonymous with the word "database" (e.g. a primetable is a database of primes)
#
# The word "data structure" is synonymous with the word "database"
#
# You could argue that, in some contexts, these words have slightly different meanings
#
# For example, a MySQL table is different from a MySQL database
#
# (A MySQL database often consists of many tables)
#
# But I think this is just an inherent feature of the English language
#
# An English language word can have many meanings
#
# The word "table" can generically refer to a database, or it can specifically refer to a MySQL table
#
# The word "table" has multiple definitions, and one definition of table is "database"
#
# So we have spent some time talking about databases
#
# Now let's talk about algorithms
#
# The binary search tree algorithms lend themselves to recursion
#
# It is possible to implement the insert, search, and balance methods in an iterative manner
#
# But it is easier and more elegant to implement these methods in a recursive manner
#
# What is recursion? What is iteration?
#
# Recursion means that a function is calling itself
#
# Iteration means that we are using a loop to repeat a set of instructions
#
# So recursion implies that a function is calling itself
#
# Iteration implies loops
#
# At the time of writing, every binary search tree algorithm contained in this file is implemented recursively
#
# I also used wrapper methods to simplify the interface
#
# The caller does not need to have a reference to the root node in order to call the tree functions
#
# It is important to see what our tree looks like, to visualize our tree, so I implemented a str() method
#
# The str() method uses prefix notation to visualize our tree
#
# (The str() method uses a preorder traversal, whereas the tolist() method uses an inorder traversal)
#
# Returning to the subject of data structures, you might ask, "Why do we have binary search trees?"
#
# Binary search trees are useful because they can reduce search time
#
# The average case performance for a binary search, in a balanced binary search tree, is O(log n)
#
# This is better than a naive search on an unsorted list, which has an average case performance of O(n)
#
# I think that even a linear search on a sorted list has an average case performance of O(n)
#
# So binary search reduces the time complexity of searching from O(n) to O(log n)
#
# I think that many databases, like Oracle and MySQL, use trees to reduce search time
#
# When we index an Oracle table or a MySQL table, it creates a search tree in the background
#
# You might ask, "Do they use binary search trees to index tables?"
#
# I think they actually use something slightly different from binary search trees
#
# I think they actually use b-trees
#
# But in theory, I think that we can use a binary search tree to index a table in a relational database
#
# In a long-running application (like a server that has constant uptime) a binary search tree can save time on searching
#
# It is common for a database to have constant uptime, so you can see why trees are used to index tables
#
# I'll say it once again... in theory, I think that we can use a binary search tree to index a database table
#
# In practice, b-trees are used, but in theory, I think that binary search trees can be used as well
#
# A good exercise would be creating a database that uses binary search trees to index tables
#
# I might get around to this sometime
#
# Anyway, I think it is time to wrap things up and summarize our discussion
#
# In these comments we asked, "What is an algorithm? What is a datastructure? What is recursion? What is iteration?"
#
# An algorithm is a list of instructions
#
# A data structure is a database
#
# Recursion means that a function is calling itself
#
# Iteration means that we are using a loop to repeat a set of instructions
#
# Binary search trees are an important type of data structure
#
# The binary search tree algorithms lend themselves well to recursion
#
# I think we can end on this note
#
# Today is Saturday, November 15, 2025
#
# I'm listening to a song called Skel by Sigur Ros
#
# I have been listening to Sigur Ros's music since high school
#
# I wish everyone a nice weekend
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
