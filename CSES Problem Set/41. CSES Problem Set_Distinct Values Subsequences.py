MOD = 10**9 + 7


def mod_inv(a):
    res = 1
    b = MOD - 2
    while b > 0:
        if b & 1:
            res = (res * a) % MOD
        a = (a * a) % MOD
        b >>= 1
    return res


def main():
    n = int(input())
    arr = list(map(int, input().split()))

    freq = {}
    ans = 0
    prod = 1

    for val in arr:
        f = freq.get(val, 0)
        seqs = (prod * mod_inv(f + 1)) % MOD
        ans = (ans + seqs) % MOD

        freq[val] = f + 1
        prod = (prod * (f + 2)) % MOD
        prod = (prod * mod_inv(f + 1)) % MOD

    print(ans % MOD)


if __name__ == "__main__":
    main()
