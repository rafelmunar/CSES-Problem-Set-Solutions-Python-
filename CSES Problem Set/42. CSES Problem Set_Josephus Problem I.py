class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 2)

    def add(self, idx, delta):
        while idx <= self.n:
            self.bit[idx] += delta
            idx += idx & -idx

    def sum(self, idx):
        s = 0
        while idx > 0:
            s += self.bit[idx]
            idx -= idx & -idx
        return s

    def total(self):
        return self.sum(self.n)

    def find_kth(self, k):
        idx = 0
        bit_mask = 1 << (self.n.bit_length())
        while bit_mask:
            next_idx = idx + bit_mask
            if next_idx <= self.n and self.bit[next_idx] < k:
                k -= self.bit[next_idx]
                idx = next_idx
            bit_mask >>= 1
        return idx + 1


def solve():
    n = int(input())

    bit = FenwickTree(n)
    for i in range(1, n + 1):
        bit.add(i, 1)

    result = []
    pos = 0

    for remaining in range(n, 0, -1):
        current_count = bit.sum(pos) if pos > 0 else 0

        next_count = (current_count + 1) % remaining + 1

        next_idx = bit.find_kth(next_count)
        result.append(next_idx)

        bit.add(next_idx, -1)

        pos = next_idx

    print(" ".join(map(str, result)))


if __name__ == "__main__":
    solve()
