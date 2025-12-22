class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)
        self.lazy = [0] * (4 * n)

    def _push(self, idx):
        if self.lazy[idx]:
            self.tree[2 * idx] += self.lazy[idx]
            self.tree[2 * idx + 1] += self.lazy[idx]
            self.lazy[2 * idx] += self.lazy[idx]
            self.lazy[2 * idx + 1] += self.lazy[idx]
            self.lazy[idx] = 0

    def _update(self, idx, l, r, ql, qr, val):
        if ql > r or qr < l:
            return
        if ql <= l and r <= qr:
            self.tree[idx] += val
            self.lazy[idx] += val
            return

        self._push(idx)
        mid = (l + r) // 2
        self._update(2 * idx, l, mid, ql, qr, val)
        self._update(2 * idx + 1, mid + 1, r, ql, qr, val)
        self.tree[idx] = max(self.tree[2 * idx], self.tree[2 * idx + 1])

    def update(self, ql, qr, val):
        self._update(1, 0, self.n - 1, ql, qr, val)

    def _query(self, idx, l, r, ql, qr):
        if ql > r or qr < l:
            return 0
        if ql <= l and r <= qr:
            return self.tree[idx]

        self._push(idx)
        mid = (l + r) // 2
        left_max = self._query(2 * idx, l, mid, ql, qr)
        right_max = self._query(2 * idx + 1, mid + 1, r, ql, qr)
        return max(left_max, right_max)

    def query(self, ql, qr):
        return self._query(1, 0, self.n - 1, ql, qr)


def main():
    n, k = map(int, input().split())
    movies = []
    all_times = []

    for i in range(n):
        a, b = map(int, input().split())
        movies.append((a, b, i))
        all_times.append(a)
        all_times.append(b)

    unique_times = sorted(set(all_times))
    time_to_idx = {t: idx for idx, t in enumerate(unique_times)}
    m = len(unique_times)

    events = []
    for a, b, idx in movies:
        events.append((a, idx, 0))
        events.append((b, idx, 1))

    events.sort(key=lambda x: (x[0], x[2], -movies[x[1]][0] if x[2] == 1 else 0))

    seg = SegmentTree(2 * m)

    ans = 0
    for time, idx, typ in events:
        if typ == 1:
            a, b, _ = movies[idx]
            start_idx = time_to_idx[a]
            end_idx = time_to_idx[b]

            max_watching = seg.query(start_idx, end_idx - 1)
            if max_watching < k:
                seg.update(start_idx, end_idx - 1, 1)
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
