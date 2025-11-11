import random
import time
import argparse
import ast

class BinarySearchTree:
    def __init__(self, arr=None):
        self.root = None
        self.arr = []
        if arr:
            self._balance(sorted(arr))

    def _balance(self, arr):
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

    def balance(self):
        tmp = self.arr
        self.root = None
        self.arr = []
        self._balance(tmp)

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
        print(f'Unsorted list:\n{arr}\n')
    elif args.random:
        size, min, max = int(args.size), int(args.minimum), int(args.maximum)
        arr = [random.randint(min, max) for i in range(size)]
        if size < 1000:
            print(f'Randomly generated list:\n{arr}\n')
    tree = BinarySearchTree(arr)
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
