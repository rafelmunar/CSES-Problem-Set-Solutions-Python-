n = int(input())
movies = []

for _ in range(n):
    a, b = map(int, input().split())
    movies.append((a, b))

movies.sort(key=lambda x: x[1])

count = 0
last_end = 0

for start, end in movies:
    if start >= last_end:
        count += 1
        last_end = end

print(count)
