def main():
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))

    pair_sums = {}

    for i in range(n):
        for j in range(i + 1, n):
            s = arr[i] + arr[j]
            if s not in pair_sums:
                pair_sums[s] = []
            pair_sums[s].append((i, j))

    for i in range(n):
        for j in range(i + 1, n):
            target = x - arr[i] - arr[j]
            if target in pair_sums:
                for k, l in pair_sums[target]:
                    if i != k and i != l and j != k and j != l:
                        indices = [i + 1, j + 1, k + 1, l + 1]
                        indices.sort()
                        print(indices[0], indices[1], indices[2], indices[3])
                        return

    print("IMPOSSIBLE")


if __name__ == "__main__":
    main()
