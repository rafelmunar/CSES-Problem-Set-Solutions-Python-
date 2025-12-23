def min_cuts(a, b):
    dp = [[float("inf")] * (b + 1) for _ in range(a + 1)]

    for i in range(1, a + 1):
        for j in range(1, b + 1):
            if i == j:
                dp[i][j] = 0

    for i in range(1, a + 1):
        for j in range(1, b + 1):
            if i == j:
                continue

            for k in range(1, j):
                dp[i][j] = min(dp[i][j], 1 + dp[i][k] + dp[i][j - k])

            for k in range(1, i):
                dp[i][j] = min(dp[i][j], 1 + dp[k][j] + dp[i - k][j])

    return dp[a][b]


def main():
    a, b = map(int, input().split())
    print(min_cuts(a, b))


if __name__ == "__main__":
    main()
