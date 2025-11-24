n = int(input())

arr = [int(x) for x in input().split()]

count = 0

for i in range(1, n):
    increase = 0
    if arr[i] < arr[i - 1]:
        increase = arr[i - 1] - arr[i]
        arr[i] += increase
        count += increase

print(count)
