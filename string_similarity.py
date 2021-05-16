# your code goes here

def possible_substring(s, n):
    return s[::2]
	
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, s = int(input()), input()
        print(possible_substring(s, n))