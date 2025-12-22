def main():
    n = int(input())
    arr = list(map(int, input().split()))

    result = [0] * n
    stack = []

    for i in range(n):
        while stack and stack[-1][0] >= arr[i]:
            stack.pop()

        if stack:
            result[i] = stack[-1][1] + 1
        else:
            result[i] = 0

        stack.append((arr[i], i))

    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
