def can_make(t, machines, time_limit):
    total = 0
    for k in machines:
        total += time_limit // k
        if total >= t:
            return True
    return total >= t


def main():
    n, t = map(int, input().split())
    machines = list(map(int, input().split()))

    left = 0
    right = 10**18

    while left < right:
        mid = (left + right) // 2
        if can_make(t, machines, mid):
            right = mid
        else:
            left = mid + 1

    print(left)


if __name__ == "__main__":
    main()
