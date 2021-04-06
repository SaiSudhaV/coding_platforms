def spiralOrder(self, A):
    row, col = len(A), len(A[0])
    top, bot, left, right = 0, row - 1, 0, col - 1
    tem, res = 0 , []
    while (top <= bot and left <= right):
        if tem == 0:
            for i in range(left, right + 1, 1):
                res.append(A[top][i])
            top += 1
            tem = 1
        elif tem == 1:
            for i in range(top, bot + 1, 1):
                res.append(A[i][right])
            right -= 1
            tem = 2
        elif tem == 2:
            for i in range(right, left - 1, -1):
                res.append(A[bot][i])
            bot -= 1
            tem = 3
        elif tem  == 3:
            for i in range(bot, top - 1, -1):
                res.append(A[i][left])
            left += 1
            tem = 0
    return res