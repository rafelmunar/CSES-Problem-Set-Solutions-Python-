def main():
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))

    prefix_count = {0: 1}
    current_sum = 0
    result = 0

    for num in arr:
        current_sum += num

        target = current_sum - x
        if target in prefix_count:
            result += prefix_count[target]

        prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1

    print(result)


if __name__ == "__main__":
    main()
