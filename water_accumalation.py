def accumulation(ar, side, height):
    return max(height, ar[side])

def waterAccumulated(ar, n):
    left, right, total = 0, n - 1, 0
    tall_in_left, tall_in_right = ar[left], ar[right]
    while left < right:
        if ar[left] <= ar[right]:
            left += 1
            tall_in_left = accumulation(ar, left, tall_in_left)
            total += tall_in_left - ar[left]
        else:
            right -= 1
            tall_in_right = accumulation(ar, right, tall_in_right)
            total += tall_in_right - ar[right]
    return total

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        ar = list(map(int, input().split()))
        print(waterAccumulated(ar, n))