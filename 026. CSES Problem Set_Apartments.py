n, m, k = map(int, input().split())
applicants = list(map(int, input().split()))
apartments = list(map(int, input().split()))

applicants.sort()
apartments.sort()

i = j = count = 0

while i < n and j < m:
    if abs(applicants[i] - apartments[j]) <= k:
        count += 1
        i += 1
        j += 1
    elif applicants[i] - apartments[j] > k:
        j += 1
    else:
        i += 1

print(count)
