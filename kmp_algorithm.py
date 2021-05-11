def find_pattern(text, n, pattern, m): 
    lps, j = [0] * m , 0
    computeLPSArray(pattern, m, lps) 
    i, count = 0, 0
    while i < n: 
        if text[i] == pattern[j]: 
            j, i = j + 1, i + 1
        if j == m: 
            j = lps[j - 1] 
            count += 1
        elif i < n and text[i] != pattern[j]:
            if j != 0: 
                j = lps[j - 1] 
            else: 
                i += 1
    return count

def computeLPSArray(pattern, m, lps):
    n, i, lps[0] = 0, 1, 0
    while i < m: 
        if pattern[i] == pattern[n]: 
            n += 1
            lps[i] = n
            i += 1
        else:
            if n != 0: 
                n = lps[n - 1] 
            else:
                lps[i] = 0
                i += 1

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        pattern, string = input().split()
        print(find_pattern(string, len(string), pattern, len(pattern)))