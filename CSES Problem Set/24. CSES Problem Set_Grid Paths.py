path = input().strip()
n = 7
visited = [[False] * n for _ in range(n)]

dirs = [(1, 0), (0, -1), (0, 1), (-1, 0)]
dir_char = ["D", "L", "R", "U"]


def dfs(x, y, step):
    if x == 6 and y == 0:
        return 1 if step == 48 else 0
    if step == 48:
        return 0

    if (
        y > 0
        and y < 6
        and not visited[x][y - 1]
        and not visited[x][y + 1]
        and ((x == 0 and visited[x + 1][y]) or (x == 6 and visited[x - 1][y]))
    ) or (
        x > 0
        and x < 6
        and not visited[x - 1][y]
        and not visited[x + 1][y]
        and ((y == 0 and visited[x][y + 1]) or (y == 6 and visited[x][y - 1]))
    ):
        return 0

    forced_move = -1
    moves = 0
    for d in range(4):
        nx, ny = x + dirs[d][0], y + dirs[d][1]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            moves += 1
            forced_move = d
    if moves == 1 and forced_move != -1:
        ch = path[step]
        if ch != "?" and ch != dir_char[forced_move]:
            return 0

    total = 0
    ch = path[step]

    for d in range(4):
        if ch != "?" and ch != dir_char[d]:
            continue

        nx, ny = x + dirs[d][0], y + dirs[d][1]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            visited[nx][ny] = True
            total += dfs(nx, ny, step + 1)
            visited[nx][ny] = False

    return total


visited[0][0] = True
print(dfs(0, 0, 0))
