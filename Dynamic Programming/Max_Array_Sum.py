def maxSubsetSum(arr):
    incl = max(0, arr[0])
    excl = 0

    for i in range(1, len(arr)):
        new_incl = arr[i] + excl
        new_excl = max(incl , excl)

        incl = new_incl
        excl = new_excl

    return max(incl, excl)

print(maxSubsetSum([3,7,4,6,5]))