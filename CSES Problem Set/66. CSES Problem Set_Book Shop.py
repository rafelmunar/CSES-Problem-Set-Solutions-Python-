def main():
    n, x = map(int, input().split())
    prices = list(map(int, input().split()))
    pages = list(map(int, input().split()))

    dp = [0] * (x + 1)

    for i in range(n):
        price = prices[i]
        page = pages[i]
        for p in range(x, price - 1, -1):
            if dp[p - price] + page > dp[p]:
                dp[p] = dp[p - price] + page

    print(dp[x])


if __name__ == "__main__":
    main()
