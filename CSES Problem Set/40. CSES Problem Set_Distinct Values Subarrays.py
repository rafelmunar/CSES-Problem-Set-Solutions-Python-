def main():
    n = int(input())
    arr = list(map(int, input().split()))

    last_seen = {}
    left = 0
    total = 0

    for right in range(n):
        if arr[right] in last_seen:
            left = max(left, last_seen[arr[right]] + 1)

        total += right - left + 1

        last_seen[arr[right]] = right

    print(total)


if __name__ == "__main__":
    main()
