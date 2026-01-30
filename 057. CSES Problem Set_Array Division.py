def can_divide(arr, k, max_sum):
    subarrays = 1
    current_sum = 0

    for num in arr:
        if current_sum + num > max_sum:
            subarrays += 1
            current_sum = num
            if subarrays > k or num > max_sum:
                return False
        else:
            current_sum += num

    return subarrays <= k


def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    low = max(arr)
    high = sum(arr)

    while low < high:
        mid = (low + high) // 2
        if can_divide(arr, k, mid):
            high = mid
        else:
            low = mid + 1

    print(low)


if __name__ == "__main__":
    main()
