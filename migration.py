def migratoryBirds(arr):
    return arr.index(max(arr))

if __name__ == '__main__':
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = migratoryBirds(arr)
    print(str(result))

