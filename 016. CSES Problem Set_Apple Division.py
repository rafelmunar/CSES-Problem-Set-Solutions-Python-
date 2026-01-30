n = int(input())

values = sorted(int(i) for i in input().split())

s = sum(values)


def minimum(s, values):
    if len(values) == 1:
        return abs(s - 2 * values[0])

    else:
        m = abs(s - 2 * values[0])
        for i in range(1, len(values)):
            m = min(m, abs(minimum(s - 2 * values[i], values[:i])))

        return m


print(minimum(s, values))
