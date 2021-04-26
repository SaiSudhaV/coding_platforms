def lucky_number(n):
    if n == 4 or n == 7:
        return True
    return False

def lucky_digits(n):
    count = 0
    lst = [i for i in n]
    for i in lst:
        if i == "4" or i == "7":
            count += 1
    return count
        
def nearly_lucky(n):
    if lucky_number(lucky_digits(n)):
        return "YES"
    return "NO"
        
if __name__ == "__main__":
    n = str(input())
    res = nearly_lucky(n)
    print(res)
