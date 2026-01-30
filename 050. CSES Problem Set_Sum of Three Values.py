def main():
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))

    values = [(arr[i], i + 1) for i in range(n)]
    values.sort(key=lambda v: v[0])

    for i in range(n - 2):
        target = x - values[i][0]
        left = i + 1
        right = n - 1

        while left < right:
            current_sum = values[left][0] + values[right][0]
            if current_sum == target:
                idx1 = values[i][1]
                idx2 = values[left][1]
                idx3 = values[right][1]
                result = sorted([idx1, idx2, idx3])
                print(result[0], result[1], result[2])
                return
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    print("IMPOSSIBLE")


if __name__ == "__main__":
    main()
