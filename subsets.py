def subsets(A):
    subset = []
    res = []
    index = 0
    calcSubset(A, res, subset, index)
    return res

def calcSubset(A, res, subset, index):
    res.append(list(subset))

    for i in range(index, len(A)):
        subset.append(A[i])
        calcSubset(A, res, subset, i+1)
        subset.pop()

if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    S = subsets(A)
    print(S)
    print("Number of subsets: %d" %len(S))