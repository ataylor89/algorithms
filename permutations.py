def permutations(arr):
    p = []
    permute(arr, 0, len(arr), p)
    return p

def permute(a, l, r, p):
    if l == r:
        p.append(list(a))
    else:
        for i in range(l, r):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r, p)
            a[l], a[i] = a[i], a[l]

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    perms = permutations(arr)
    print(perms)
    print("Number of permutations: %d" %len(perms))