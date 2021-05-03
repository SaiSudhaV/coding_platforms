def stonesOnTable(s):
    count = 0
    for i in range(0,len(s)-1):
        if s[i]== s[i+1]:
          count = count + 1
    return count
 
if __name__ == "__main__":
     n = int(input())
     s = input()
     print(stonesOnTable(s))
