def triplets(a, b, c):
    count = 0
    a = sorted(set(a))
    b = sorted(set(b))
    c = sorted(set(c))

    pa = pc = 0 
    for val in b:
        while pa < len(a) and val >= a[pa]:
            pa += 1
        while pc < len(c) and val >= c[pc]:
            pc += 1
        count += pa * pc
    return count

print(triplets([1,3,5], [2,3], [1,2,3]))