def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    freq = {}
    distinct = 0
    left = 0
    total = 0

    for right in range(n):
        if arr[right] not in freq or freq[arr[right]] == 0:
            distinct += 1
        freq[arr[right]] = freq.get(arr[right], 0) + 1

        while distinct > k:
            freq[arr[left]] -= 1
            if freq[arr[left]] == 0:
                distinct -= 1
            left += 1

        total += right - left + 1

    print(total)


if __name__ == "__main__":
    main()
