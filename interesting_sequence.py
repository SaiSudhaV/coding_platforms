# cook your dish here

def subsequence_sum(n):
    k = 4 * (n + 1)
    tem, res = [0] * k, [0] * k
    for i in range(k):
        tem[i], res[i] = i, 0
    for i in range(2, k):
        if tem[i] == i:
            tem[i] = i - 1
            j = 2 * i
            while j < k:
                tem[j] = (tem[j] // i) * (i - 1)
                j += i
    for i in range(1, k):
        res[i] += i - 1
        for j in range(2 * i, k, i):
            res[j] += i * ((1 + tem[j // i]) // 2)
    return res[k - 3]

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        print(subsequence_sum(n))