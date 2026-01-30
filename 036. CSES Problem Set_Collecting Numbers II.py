n, m = map(int, input().split())
arr = list(map(int, input().split()))

pos = [0] * (n + 1)
for i in range(n):
    pos[arr[i]] = i

count = 0
for i in range(1, n):
    if pos[i] > pos[i + 1]:
        count += 1


def update(val, delta):
    global count
    if 1 <= val < n:
        if pos[val] > pos[val + 1]:
            count += delta


for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    x, y = arr[a], arr[b]

    affected = set()
    for val in [x - 1, x, y - 1, y]:
        affected.add(val)

    for val in affected:
        update(val, -1)

    arr[a], arr[b] = arr[b], arr[a]
    pos[x], pos[y] = pos[y], pos[x]

    for val in affected:
        update(val, 1)

    print(count + 1)
