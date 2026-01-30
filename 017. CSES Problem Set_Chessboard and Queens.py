board = [input().strip() for _ in range(8)]


def solve(board, row, occupiedCol, occupiedPrimary, occupiedSecondary, ans):
    if row == 8:
        ans[0] += 1
        return
    for col in range(8):
        if (
            board[row][col] == "*"
            or occupiedCol[col]
            or occupiedPrimary[row - col + 8]
            or occupiedSecondary[row + col]
        ):
            continue
        occupiedCol[col] = True
        occupiedPrimary[row - col + 8] = True
        occupiedSecondary[row + col] = True

        solve(board, row + 1, occupiedCol, occupiedPrimary, occupiedSecondary, ans)

        occupiedCol[col] = False
        occupiedPrimary[row - col + 8] = False
        occupiedSecondary[row + col] = False


occupiedCol = [False] * 8
occupiedPrimary = [False] * 20
occupiedSecondary = [False] * 20
ans = [0]

solve(board, 0, occupiedCol, occupiedPrimary, occupiedSecondary, ans)
print(ans[0])
