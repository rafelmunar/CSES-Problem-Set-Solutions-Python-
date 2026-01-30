MOD = 10**9 + 7


def main():
    n, x = map(int, input().split())
    coins = list(map(int, input().split()))

    dp = [0] * (x + 1)
    dp[0] = 1

    for s in range(1, x + 1):
        for c in coins:
            if s - c >= 0:
                dp[s] = (dp[s] + dp[s - c]) % MOD

    print(dp[x] % MOD)


if __name__ == "__main__":
    main()
