# cook your dish here

def count_steps(s, n):
    count1, count2, tem = 0, 0, ''
    for i in range(n):
        if s[i] != tem:
            if s[i] == 'U':
                count1, tem = count1 + 1, 'U'
            elif s[i] == 'D':
                count2, tem = count2 + 1, 'D'
    return min(count1, count2)

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        s = input()
        print(count_steps(s, len(s)))