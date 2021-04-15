def boyOrGirl(s):
    s1 = "".join([i for i in sorted([i for i in s])])
    count = 1
    for i in range(len(s1) - 1):
        if s1[i] != s1[i + 1]:
            count += 1
    return "CHAT WITH HER!" if count % 2 == 0 else "IGNORE HIM!"

if __name__ == "__main__":
    s = input()
    print(boyOrGirl(s))
