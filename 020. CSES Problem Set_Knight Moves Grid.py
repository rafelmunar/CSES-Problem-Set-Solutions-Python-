n = int(input)

dist = [[-1] * n for _ in range(n)]
moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

queue = [(0, 0)]
dist[0][0] = 0
idx = 0

while idx < len(queue):
    x, y = queue[idx]
    idx += 1
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            queue.append((nx, ny))

for row in dist:
    print(" ".join(map(str, row)))
