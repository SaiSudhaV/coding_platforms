def explode(grid, n):
    grid = [i.replace('O', '2') for i in grid]
    grid = [i.replace('.', '0') for i in grid]
    grid = [list(map(int, list(i))) for i in grid]
    row, col, tem = len(grid), len(grid[0]), 1
    while tem < 4 + (n % 4):
        tem += 1
        res = []
        for i in range(row):
            for j in range(col):
                if grid[i][j] > 0:
                    grid[i][j] -= 1
                if tem % 2 == 0 and grid[i][j] == 0:
                    grid[i][j] = 3
                elif grid[i][j] == 0:
                    res.append([i, j])
                    if i < row - 1:
                        res.append([i + 1, j])
                    if i > 0:
                        res.append([i - 1, j])
                    if j < col - 1:
                        res.append([i , j + 1])
                    if j > 0:
                        res.append([i, j - 1])
        if res:
            grid = [[2] * len(i) for i in grid]
            for i, j in res:
                grid[i][j] = 0
    grid = [''.join(list(map(str, i))) for i in grid]
    grid = [i.replace('2', 'O') for i in grid]
    grid = [i.replace('0', '.') for i in grid]
    return grid

def bomberMan(n, grid):
    return grid if n in [0, 1] else ['O' * len(x) for x in grid] if n % 2 == 0 else explode(grid, n)

if __name__ == '__main__':
    r, c, n = map(int, input().split())
    grid = []
    for _ in range(r):
        grid_input = input()
        grid.append(grid_input)
    print('\n'.join(bomberMan(n, grid)))
