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
        if arr:
            self.balance(arr)
        else:
            self.root = None
            self.arr = []

    def balance(self, arr=None):
        self.root = None
        if arr is None:
            arr = self.arr
        self.arr = []
        arr.sort()
        sieve = [False] * len(arr)
        delta = int(len(arr) / 2)
        while delta > 0:
            n = 1
            while n * delta < len(arr):
                index = n * delta
                if not sieve[index]:
                    self.insert(arr[index])
                    sieve[index] = True
                n += 1
            delta = int(delta/2)
        self.insert(arr[0])

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            self.arr.append(value)
            return
        node = self.root
        while node:
            if value <= node.value and node.left is None:
                node.left = Node(value)
                self.arr.append(value)
                return
            elif value <= node.value:
                node = node.left
            elif value > node.value and node.right is None:
                node.right = Node(value)
                self.arr.append(value)
                return
            elif value > node.value:
                node = node.right
    
    def search(self, value):
        if self.root is None:
            return False
        node = self.root
        while node:
            if value == node.value:
                return True
            elif value < node.value:
                node = node.left
            elif value > node.value:
                node = node.right
        return False

    def _height(self, node, height):
        if node is None:
            return
        height += 1
        if height > self.h:
            self.h = height
        self._height(node.left, height)
        self._height(node.right, height)

    def height(self):
        self.h = 0
        self._height(self.root, 0)
        return self.h

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='bst.py', description='Binary search')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-i', '--inputfile', type=str)
    group.add_argument('-n', '--numbers', nargs='+', type=int) 
    group.add_argument('-r', '--random', action='store_true')
    parser.add_argument('-s', '--size', type=float, default=10)
    parser.add_argument('-min', '--minimum', type=float, default=0)
    parser.add_argument('-max', '--maximum', type=float, default=100)
    parser.add_argument('-t', '--test', nargs='+', type=int, required=True) 
    args = parser.parse_args()
    if args.inputfile:
        with open(args.inputfile, 'r') as file:
            contents = file.read()
            arr = ast.literal_eval(contents)
    elif args.numbers:
        arr = args.numbers
        print(f'Unsorted list:\n\n{arr}\n')
    elif args.random:
        size, min, max = int(args.size), int(args.minimum), int(args.maximum)
        arr = [random.randint(min, max) for i in range(size)]
        if size < 1000:
            print(f'Randomly generated list:\n\n{arr}\n')
    tree = BinarySearchTree(arr)
    height = tree.height()
    print(f'The binary search tree has a height of {height}\n')
    print('Linear search\n--------------')
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
    print('Binary search\n--------------')
    for i in range(len(args.test)):
        value = args.test[i]
        start_time = time.time()
        found = tree.search(value)
        time_elapsed = 1000 * (time.time() - start_time)
        print(f'{value} is present' if found else f'{value} is missing')
        print(f'The binary search took {time_elapsed:.4f} milliseconds')
        if i < len(args.test) - 1:
            print('')
