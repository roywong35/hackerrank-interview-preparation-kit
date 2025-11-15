def whatFlavors(cost, money):
    seen = {}
    for i, val in enumerate(cost):
        complement = money - val
        if complement not in seen:
            seen[val] = i
        else:
            a = seen[complement] + 1
            b = i + 1
            print(a, b)
    
whatFlavors([1, 4, 5, 3, 2], 4)