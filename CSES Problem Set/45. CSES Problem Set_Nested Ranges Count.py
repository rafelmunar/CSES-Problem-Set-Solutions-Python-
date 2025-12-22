class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 2)

    def add(self, idx, delta):
        i = idx
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def sum(self, idx):
        s = 0
        i = idx
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def range_sum(self, l, r):
        if l > r:
            return 0
        return self.sum(r) - self.sum(l - 1)


def main():
    n = int(input())
    ranges = []
    all_ys = []

    for i in range(n):
        x, y = map(int, input().split())
        ranges.append((x, y, i))
        all_ys.append(y)

    sorted_ys = sorted(set(all_ys))
    y_to_idx = {y: idx + 1 for idx, y in enumerate(sorted_ys)}
    m = len(sorted_ys)

    contains_cnt = [0] * n
    contained_cnt = [0] * n

    sorted_by_x_desc_y = sorted(ranges, key=lambda r: (r[0], -r[1]))

    bit1 = BIT(m)

    for i in range(n - 1, -1, -1):
        x, y, idx = sorted_by_x_desc_y[i]
        y_pos = y_to_idx[y]

        count = bit1.sum(y_pos)
        contains_cnt[idx] = count

        bit1.add(y_pos, 1)

    sorted_by_x_asc_y = sorted(ranges, key=lambda r: (r[0], r[1]))

    bit2 = BIT(m)

    for i in range(n):
        x, y, idx = sorted_by_x_asc_y[i]
        y_pos = y_to_idx[y]

        mayores_o_iguales = bit2.range_sum(y_pos, m)
        contained_cnt[idx] = mayores_o_iguales

        bit2.add(y_pos, 1)

    print(" ".join(map(str, contains_cnt)))
    print(" ".join(map(str, contained_cnt)))


if __name__ == "__main__":
    main()
