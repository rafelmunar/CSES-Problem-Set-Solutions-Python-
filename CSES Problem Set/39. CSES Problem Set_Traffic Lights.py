def binary_search(arr, val):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < val:
            lo = mid + 1
        else:
            hi = mid
    return lo


def main():
    x_str = input().strip()
    while x_str == "":
        x_str = input().strip()

    x_n = x_str.split()
    x = int(x_n[0])
    n = int(x_n[1])

    positions = list(map(int, input().split()))

    length_counts = []

    def get_count(length):
        for i, (key, cnt) in enumerate(length_counts):
            if key == length:
                return i, cnt
        return -1, 0

    def add_length(length):
        nonlocal max_len
        idx, cnt = get_count(length)
        if cnt == 0:
            length_counts.append([length, 1])
            if length > max_len:
                max_len = length
        else:
            length_counts[idx][1] = cnt + 1

    def remove_length(length):
        nonlocal max_len
        idx, cnt = get_count(length)
        if cnt == 1:
            length_counts[idx] = length_counts[-1]
            length_counts.pop()
            if length == max_len:
                new_max = 0
                for key, cnt2 in length_counts:
                    if cnt2 > 0 and key > new_max:
                        new_max = key
                max_len = new_max
        else:
            length_counts[idx][1] = cnt - 1

    length_counts.append([x, 1])
    max_len = x

    lights = []
    answers = []

    for p in positions:
        idx = binary_search(lights, p)

        left = lights[idx - 1] if idx > 0 else 0
        right = lights[idx] if idx < len(lights) else x

        old_len = right - left
        remove_length(old_len)

        len1 = p - left
        len2 = right - p
        if len1 > 0:
            add_length(len1)
        if len2 > 0:
            add_length(len2)

        lights.insert(idx, p)

        answers.append(max_len)

    print(" ".join(map(str, answers)))


if __name__ == "__main__":
    main()
