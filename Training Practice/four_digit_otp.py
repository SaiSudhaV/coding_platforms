# 12 You will be given a number in the form of string, extract out digits at odd places, square & merge them. First 4 digits will be the required OTP.

def gen_OTP(ar, n):
    tem = [int(ar[i]) for i in range(n) if i % 2 != 0]
    res = "".join(str(i * i) for i in tem)
    return res[:4]

if __name__ == "__main__":
    s = input()
    print(gen_OTP(list(s), len(s)))