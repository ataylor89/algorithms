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
            self.height = 0

    def balance(self, arr=None):
        self.root = None
        if arr is None:
            arr = self.arr
        self.arr = []
        self.height = 0
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
            self.height = 1
            return
        node = self.root
        height = 1
        done = False
        while not done:
            if value == node.value:
                node.frequency += 1
                self.arr.append(value)
                done = True
            elif value < node.value and node.left is None:
                node.left = Node(value)
                self.arr.append(value)
                height += 1
                done = True
            elif value < node.value:
                node = node.left
                height += 1
            elif value > node.value and node.right is None:
                node.right = Node(value)
                self.arr.append(value)
                height += 1
                done = True
            elif value > node.value:
                node = node.right
                height += 1
        if height > self.height:
            self.height = height

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
        root_value = self.root.value
        size = len(self.arr)
        height = self.height
        return f'Root value: {root_value} Size: {size} Height: {height}'

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
    if len(arr) <= 1000:
        print('')
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
