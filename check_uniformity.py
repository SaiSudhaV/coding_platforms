# cook your dish here

def check_uniformity(s):
    count, tem = 0, [s[0]]
    for i in s[1:]:
        if i != tem[-1]:
            count += 1
        tem.append(i)
    return "non-uniform" if count > 2 else "uniform"

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        s = input()
        print(check_uniformity(s))