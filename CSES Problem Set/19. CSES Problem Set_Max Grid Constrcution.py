n = int(input())


def build_grid(n):
    grid = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            left_values = set()
            for k in range(j):
                left_values.add(grid[i][k])

            above_values = set()
            for k in range(i):
                above_values.add(grid[k][j])

            num = 0
            while num in left_values or num in above_values:
                num += 1

            grid[i][j] = num

    return grid


grid = build_grid(n)

for row in grid:
    print(" ".join(str(x) for x in row))
