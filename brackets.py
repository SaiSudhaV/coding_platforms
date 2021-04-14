# cook your dish here

def brackets(s):
    count = max_count = 0
    for i in s:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
        max_count = max(max_count, count)
    return "".join(['(' for i in range(max_count)] + [')' for i in range(max_count)])
if _name_ == "_main_":
    t = int(input())
    for i in range(t):
        s = input()
        print(brackets(s))