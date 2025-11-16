def candies(n, arr):
    candies = [1] * n

    for i in range(1, n):
        if arr[i] > arr[i-1]:
            candies[i] = candies[i-1] + 1

    for j in range(n-2, -1 , -1):
        if arr[j] > arr[j+1]:
            candies[j] = max(candies[j], candies[j+1] + 1)
    return sum(candies)
print(candies(3, [1,2,2]))