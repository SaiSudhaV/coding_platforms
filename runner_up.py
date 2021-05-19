def runnerUp(ar, n):
    return sorted(ar)[-2]

if __name__ == '__main__':
    n = int(input())
    ar = map(int, input().split())
    print(runnerUp(list(set(ar)), n))