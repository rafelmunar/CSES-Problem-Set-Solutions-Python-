class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 2)

    def add(self, idx, delta):
        i = idx
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def prefix_sum(self, idx):
        s = 0
        i = idx
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def total(self):
        return self.prefix_sum(self.n)

    def find_kth(self, k):
        idx = 0
        bit_mask = 1
        while bit_mask <= self.n:
            bit_mask <<= 1
        bit_mask >>= 1

        while bit_mask > 0:
            next_idx = idx + bit_mask
            if next_idx <= self.n and self.tree[next_idx] < k:
                k -= self.tree[next_idx]
                idx = next_idx
            bit_mask >>= 1
        return idx + 1


def main():
    try:
        data = input().strip().split()
    except EOFError:
        return

    if not data:
        return

    n = int(data[0])
    k = int(data[1]) if len(data) > 1 else 0

    if k == 0:
        print(" ".join(str(i) for i in range(1, n + 1)))
        return

    bit = BIT(n)
    for i in range(1, n + 1):
        bit.add(i, 1)

    result = []
    current_pos = 0
    remaining = n

    for _ in range(n):
        next_pos = (current_pos + k) % remaining

        idx = bit.find_kth(next_pos + 1)
        result.append(str(idx))

        bit.add(idx, -1)

        current_pos = next_pos
        remaining -= 1

    print(" ".join(result))


if __name__ == "__main__":
    main()
