def main():
    n, x = map(int, input().split())
    coins = list(map(int, input().split()))

    INF = 10**9
    dp = [INF] * (x + 1)
    dp[0] = 0

    for s in range(1, x + 1):
        for c in coins:
            if s - c >= 0:
                dp[s] = min(dp[s], dp[s - c] + 1)

    result = dp[x] if dp[x] != INF else -1
    print(result)


if __name__ == "__main__":
    main()
