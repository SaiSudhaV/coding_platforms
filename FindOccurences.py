# your code goes here
 
def findOccurences(s1, s2, n):
    res, tem = [], s2.find(s1)
    if not tem > 0:
        return ""
    while tem > 0:
        res.append(tem)
        tem = s2.find(s1, tem + 1)
    return "\n".join(str(i) for i in res)
    
if __name__ == "__main__":
    while True:
        try:
            n, s1, s2 = int(input()), input(), input()
            print(findOccurences(s1, s2, n))
        except:
            break