if __name__ == "__main__":
    year = int(input())
    while(True):
        year = str(int(year) + 1)
        s, s1, s2, s3 = year[0], year[1], year[2], year[3]
        if year.count(s) == year.count(s1) == year.count(s2) == year.count(s3) == 1:
            break
    print(year)
