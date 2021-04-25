def acBall(lst1, lst2):
    result = ''
    for i, j in zip(lst1, lst2):
        if i == 'W' and j == 'W':
            result += 'B'
        elif i == 'B' and j == 'B':
            result += 'W'
        else:
            result += 'B'
    return result
    
if __name__ == '__main__':
    t = int (input())
    for i in range(t):
        in1 = list(input())
        in2 = list(input())
        print(acBall(in1, in2))
