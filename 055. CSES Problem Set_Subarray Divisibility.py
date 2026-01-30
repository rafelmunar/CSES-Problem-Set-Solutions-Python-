def main():
    n = int(input())
    arr = list(map(int, input().split()))

    residue_count = {0: 1}
    current_sum = 0

    for num in arr:
        current_sum += num
        residue = current_sum % n
        residue_count[residue] = residue_count.get(residue, 0) + 1

    total = 0
    for count in residue_count.values():
        total += count * (count - 1) // 2

    print(total)


if __name__ == "__main__":
    main()
