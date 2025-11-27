t = int(input())

for _ in range(t):
    n, a, b = map(int, input().split())

    if a + b > n:
        print("NO")
        continue

    if n == 1:
        if a == 0 and b == 0:
            print("YES")
            print("1")
            print("1")
        else:
            print("NO")
        continue

    if a == n or b == n:
        print("NO")
        continue

    if a == 0 and b != 0:
        print("NO")
        continue

    if b == 0 and a != 0:
        print("NO")
        continue

    p1 = list(range(1, n + 1))
    p2 = list(range(1, n + 1))

    res1 = []
    res2 = []

    ties = n - a - b

    for i in range(ties):
        res1.append(p1[i])
        res2.append(p2[i])

    for i in range(a):
        res1.append(p1[ties + i + b])
        res2.append(p2[i])

    for i in range(b):
        res1.append(p1[ties + i])
        res2.append(p2[ties + a + i])

    valid = True

    score1 = 0
    score2 = 0
    for c1, c2 in zip(res1, res2):
        if c1 > c2:
            score1 += 1
        elif c2 > c1:
            score2 += 1
    if score1 != a or score2 != b:
        print("NO")
        continue

    print("YES")
    print(" ".join(map(str, res1)))
    print(" ".join(map(str, res2)))
