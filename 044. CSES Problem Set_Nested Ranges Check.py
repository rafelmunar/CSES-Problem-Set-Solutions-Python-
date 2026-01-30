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
        return self.sum(r) - self.sum(l - 1)


def main():
    n = int(input())
    ranges = []
    all_ends = []

    for i in range(n):
        x, y = map(int, input().split())
        ranges.append((x, y, i))
        all_ends.append(y)

    sorted_ends = sorted(set(all_ends))
    end_to_idx = {val: idx + 1 for idx, val in enumerate(sorted_ends)}  # 1-based

    contains_other = [0] * n
    contained_by_other = [0] * n

    sorted_by_start = sorted(ranges, key=lambda r: (r[0], -r[1]))

    bit1 = BIT(len(sorted_ends))

    max_y_so_far = -1
    for i in range(n - 1, -1, -1):
        x, y, idx = sorted_by_start[i]
        y_pos = end_to_idx[y]

        count_smaller_y = bit1.sum(y_pos)
        if count_smaller_y > 0:
            contains_other[idx] = 1

        bit1.add(y_pos, 1)

    sorted_by_start_asc = sorted(ranges, key=lambda r: (r[0], r[1]))

    max_y_seen = -1

    sorted_for_contained = sorted(ranges, key=lambda r: (r[0], -r[1]))

    bit2 = BIT(len(sorted_ends))

    max_y_so_far = -1
    min_y_for_max_x = {}

    processed = []
    for x, y, idx in sorted_for_contained:
        y_pos = end_to_idx[y]

        mayores_o_iguales = bit2.range_sum(y_pos, len(sorted_ends))

        if mayores_o_iguales > 0:
            contained_by_other[idx] = 1

        bit2.add(y_pos, 1)
        processed.append((x, y, idx))

    print(" ".join(map(str, contains_other)))
    print(" ".join(map(str, contained_by_other)))


if __name__ == "__main__":
    main()
