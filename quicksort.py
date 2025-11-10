# Quicksort is probably my favorite sorting algorithm
# It's right up there with merge sort as one of the fastest and most efficient sorting algorithms
#
# Quicksort has an average case performance of O(n log n) and a worst case performance of O(n^2)
# I think that merge sort has an average case performance of O(n log n) and a worst case performance of O(n log n)
#
# Merge sort has a better worst case performance than quicksort, but...
# Quicksort has the advantage that it uses less memory than merge sort
#
# Honestly, it is very difficult to memorize a sorting algorithm
# Also, it is very difficult to write a sorting algorithm from scratch if you forget the implementation
#
# I would like to commit quicksort to memory, because it is very useful to know a sorting algorithm
#
# There are so many sorting algorithms out there (quicksort, mergesort, heapsort, bubblesort),
# but I think that quicksort is the algorithm that I want to commit to memory
#
# Quicksort is the algorithm that I want to memorize, because it is very fast, very efficient,
# and it makes more sense to me than many other sorting algorithms
#
# Algorithms are a really important part of computer science
#
# In my opinion, an algorithm is a list of instructions
# In my opinion, a data structure is just a database
#
# I am familiar with many algorithms in cryptography (rsa, xor, rot13, rot88)
# I am also familiar with many algorithms in searching and sorting (quicksort, binary search, searching a graph, etc)
#
# It is really rewarding to learn more about algorithms and data structures
# Algorithms and data structures are an essential part of computer science
#
# ###### Examples ######
#
# Example #1:
#
# % python quicksort.py -n 12 3 7 20 40 5 26 29
# Unsorted list:
# [12, 3, 7, 20, 40, 5, 26, 29]
#
# Sorted list:
# [3, 5, 7, 12, 20, 26, 29, 40]
#
# The quicksort algorithm completed in 0.0081 milliseconds
#
# Example #2:
#
# % python quicksort.py -r -s 10 -min 0 -max 10
# Randomly generated list:
# [10, 7, 1, 5, 5, 10, 8, 3, 8, 1]
#
# Sorted list:
# [1, 1, 3, 5, 5, 7, 8, 8, 10, 10]
#
# The quicksort algorithm completed in 0.0088 milliseconds
#
# Example #3:
#
# % cat unsorted.txt
# [6, 8, 1, 10, 8, 6, 7, 0, 0, 9]
#
# % python quicksort.py -i unsorted.txt
# Sorted list:
# [0, 0, 1, 6, 6, 7, 8, 8, 9, 10]
#
# The quicksort algorithm completed in 0.0100 milliseconds
#
# Example #4:
#
# % python quicksort.py -i unsorted.txt -o sorted.txt
# The quicksort algorithm completed in 0.0091 milliseconds

import random
import time
import argparse
import ast

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)
    swap(arr, i + 1, high)
    return i + 1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='quicksort.py', description='Sort a list')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-i', '--inputfile', type=str)
    group.add_argument('-n', '--numbers', nargs='+', type=int) 
    group.add_argument('-r', '--random', action='store_true')
    parser.add_argument('-s', '--size', type=float, default=10)
    parser.add_argument('-min', '--minimum', type=float, default=0)
    parser.add_argument('-max', '--maximum', type=float, default=100)
    parser.add_argument('-o', '--outputfile', type=str)
    args = parser.parse_args()
    if args.inputfile:
        with open(args.inputfile, 'r') as file:
            contents = file.read()
            arr = ast.literal_eval(contents)
    elif args.numbers:
        arr = args.numbers
        print(f'Unsorted list:\n{arr}\n')
    elif args.random:
        arr = []
        size, min, max = int(args.size), int(args.minimum), int(args.maximum)
        for i in range(0, size):
            arr.append(random.randint(min, max))
        print(f'Randomly generated list:\n{arr}\n')
    start_time = time.time()
    quicksort(arr, 0, len(arr) - 1)
    time_elapsed = 1000 * (time.time() - start_time)
    if args.outputfile:
        with open(args.outputfile, 'w') as file:
            file.write(f'{arr}')
    else:
        print(f'Sorted list:\n{arr}\n')
    print(f'The quicksort algorithm completed in {time_elapsed:.4f} milliseconds')
