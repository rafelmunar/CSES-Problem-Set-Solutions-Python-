s = input().strip()
n = len(s)

freq = [0] * 26
for ch in s:
    freq[ord(ch) - ord("A")] += 1

if max(freq) > (n + 1) // 2:
    print(-1)
else:
    res = []
    last = -1
    for _ in range(n):
        for c in range(26):
            if freq[c] > 0 and c != last:
                freq[c] -= 1
                max_remain = max(freq)
                total_remain = sum(freq)
                if max_remain <= (total_remain + 1) // 2:
                    res.append(chr(ord("A") + c))
                    last = c
                    break
                else:
                    freq[c] += 1
    print("".join(res))
