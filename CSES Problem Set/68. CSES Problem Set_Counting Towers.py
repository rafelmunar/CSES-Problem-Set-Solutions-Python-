MOD = 10**9 + 7


def main():
    t = int(input())
    tests = []
    max_n = 0

    for _ in range(t):
        n = int(input())
        tests.append(n)
        if n > max_n:
            max_n = n

    dp = [0] * (max_n + 1)
    if max_n >= 1:
        dp[1] = 2
    if max_n >= 2:
        dp[2] = 8

    for i in range(3, max_n + 1):
        dp[i] = (6 * dp[i - 1] - 7 * dp[i - 2]) % MOD

    for n in tests:
        print(dp[n])


if __name__ == "__main__":
    main()
