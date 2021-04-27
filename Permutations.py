# cook your dish here
def permut(lst):
    for i in range(len(lst)):
        if (i + 1)!=lst[lst[i] - 1]:
            return ('not ambiguous')
    return ('ambiguous')

if __name__ == '__main__':
    s = ''
    while 1:
        n = int(input())
        if n == 0:
            break
        lst = list(map(int,input().split()))
        s += (permut(lst)) + '\n'
    print(s)
    