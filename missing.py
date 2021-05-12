def missing(lst):
    largest = max(lst)
    smallest = min(lst)
    lst1 = [int(i) for i in range(int(smallest), int(largest) + 1, 1)]
    missinglst = [i for i in lst1 if i not in lst]
    return ' '.join([str(i) for i in list(missinglst)])

if __name__ == '__main__':
    
    ilst = input().split()
    
    lst = [int(i) for i in ilst]
    result = missing(lst)
    
    print(result)
