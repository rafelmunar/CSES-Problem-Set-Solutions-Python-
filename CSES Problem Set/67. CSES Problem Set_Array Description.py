MOD = 10**9 + 7


def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    dp = [[0] * (m + 2) for _ in range(n + 1)]

    if arr[0] == 0:
        for v in range(1, m + 1):
            dp[1][v] = 1
    else:
        dp[1][arr[0]] = 1

    for i in range(2, n + 1):
        if arr[i - 1] == 0:
            for v in range(1, m + 1):
                dp[i][v] = (dp[i - 1][v - 1] + dp[i - 1][v] + dp[i - 1][v + 1]) % MOD
        else:
            v = arr[i - 1]
            dp[i][v] = (dp[i - 1][v - 1] + dp[i - 1][v] + dp[i - 1][v + 1]) % MOD

    result = 0
    for v in range(1, m + 1):
        result = (result + dp[n][v]) % MOD

    print(result)


if __name__ == "__main__":
    main()
