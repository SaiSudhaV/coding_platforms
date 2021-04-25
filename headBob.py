def headBob(st, n):
   return 'NOT INDIAN' if 'Y' in st else 'INDIAN' if 'I' in st else 'NOT SURE'
   
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        st = input()
        print(headBob(st, n))