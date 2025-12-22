def main():
    n = int(input())

    dp = [0] * (n + 1)

    for x in range(1, n + 1):
        digits = set()
        temp = x
        while temp > 0:
            digit = temp % 10
            if digit > 0:
                digits.add(digit)
            temp //= 10

        min_steps = 10**9
        for d in digits:
            min_steps = min(min_steps, dp[x - d])
        dp[x] = min_steps + 1

    print(dp[n])


if __name__ == "__main__":
    main()
