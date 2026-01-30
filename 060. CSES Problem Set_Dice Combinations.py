MOD = 10**9 + 7


def main():
    n = int(input())

    if n == 0:
        print(1)
        return

    dp = [0] * (n + 1)
    dp[0] = 1  # forma vacía

    for i in range(1, n + 1):
        for j in range(1, 7):
            if i - j >= 0:
                dp[i] = (dp[i] + dp[i - j]) % MOD

    print(dp[n] % MOD)


if __name__ == "__main__":
    main()
