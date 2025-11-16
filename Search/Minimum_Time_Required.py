def minTime(machines, goal):
    low = 1
    high = min(machines) * goal

    while low < high:
        mid = (low + high) // 2

        total = 0
        for m in machines:
            total += mid // m
            if total >= goal:  
                break

        if total >= goal:
            high = mid
        else:   
            low = mid + 1   

    return low

print(minTime([2,3], 5))

