n = int(input())

s = (n * (n + 1)) // 2

if s % 2 == 0:
    subset_sum = s // 2
    a = []
    b = []
    for i in range(n, 0, -1):
        if i <= subset_sum:
            subset_sum -= i
            a.append(i)
        else:
            b.append(i)

    print("YES")
    print(len(a))
    print(*a)
    print(len(b))
    print(*b)
else:
    print("NO")
