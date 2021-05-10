import sys
size = int(input())

star = "*"

nextLine = "\n"

def stars(n: int) -> str:
    return (n + 1) * star

def halfDiamond(size: int) -> str:
    return nextLine.join(stars(line_num) for row_num in range(size) for line_num in range(size - row_num - 1))

print(halfDiamond(size))
