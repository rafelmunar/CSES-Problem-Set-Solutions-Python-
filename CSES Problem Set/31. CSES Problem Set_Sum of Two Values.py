n, x = map(int, input().split())
arr = list(map(int, input().split()))

seen = {}

for i in range(n):
    complement = x - arr[i]

    if complement in seen:
        print(seen[complement] + 1, i + 1)
        exit()

    seen[arr[i]] = i

print("IMPOSSIBLE")
