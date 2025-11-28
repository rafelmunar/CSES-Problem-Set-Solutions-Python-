n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

result = [[""] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if (i + j) % 2 == 0:
            if grid[i][j] == "A":
                result[i][j] = "B"
            else:
                result[i][j] = "A"
        else:
            if grid[i][j] == "C":
                result[i][j] = "D"
            else:
                result[i][j] = "C"

for row in result:
    print("".join(row))
