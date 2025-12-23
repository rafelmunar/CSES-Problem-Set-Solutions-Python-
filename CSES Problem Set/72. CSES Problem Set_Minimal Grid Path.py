def main():
    n = int(input())
    grid = [input().strip() for _ in range(n)]

    INF = chr(ord("Z") + 1) * (2 * n)

    best = [[INF] * n for _ in range(n)]
    best[n - 1][n - 1] = grid[n - 1][n - 1]

    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if i == n - 1 and j == n - 1:
                continue

            candidates = []
            if j + 1 < n:
                candidates.append(grid[i][j] + best[i][j + 1])
            if i + 1 < n:
                candidates.append(grid[i][j] + best[i + 1][j])

            if candidates:
                best[i][j] = min(candidates)

    print(best[0][0])


if __name__ == "__main__":
    main()
