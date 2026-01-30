def main():
    n = int(input())
    t = list(map(int, input().split()))

    S = sum(t)
    t_max = max(t)

    result = max(S, 2 * t_max)
    print(result)


if __name__ == "__main__":
    main()
