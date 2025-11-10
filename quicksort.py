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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="quicksort.py", description="Sort a list")
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
