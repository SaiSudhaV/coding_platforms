#your code goes here
 
def min_distance(ar):
    return max(ar) - min(ar)
 
if __name__ == "__main__":
    ar = list(map(int, input().split()))
    print(min_distance(ar))