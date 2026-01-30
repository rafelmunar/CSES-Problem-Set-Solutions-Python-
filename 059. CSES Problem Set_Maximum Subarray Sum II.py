def main():
    n, a, b = map(int, input().split())
    arr = list(map(int, input().split()))

    pre = [0] * (n + 1)
    for i in range(1, n + 1):
        pre[i] = pre[i - 1] + arr[i - 1]

    dq = []
    best = -(10**18)

    for j in range(a, n + 1):
        k_max = j - a

        while dq and pre[dq[-1]] >= pre[k_max]:
            dq.pop()
        dq.append(k_max)

        k_min = j - b

        while dq and dq[0] < k_min:
            dq.pop(0)

        if dq:
            current_sum = pre[j] - pre[dq[0]]
            if current_sum > best:
                best = current_sum

    print(best)


if __name__ == "__main__":
    main()
