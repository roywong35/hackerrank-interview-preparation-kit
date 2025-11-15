def pairs(k, arr):
    seen = {}
    count = 0
    for i, val in enumerate(arr):
        comp1 = k + val
        comp2 = val - k
        seen[val] = i

        if comp1 in seen:
            count += 1
        if comp2 in seen:
            count += 1
            
    return count

print(pairs(2, [1,5,3,4,2]))

def pairs(k, arr):
    s = set(arr)
    count = 0
    for x in arr:
        if x + k in s:
            count += 1
    return count

print(pairs(2, [1,5,3,4,2]))