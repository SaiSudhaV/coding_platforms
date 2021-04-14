def neighbour(n):
    berth = {1 : '4LB', 2 : '5MB', 3 : '6UB', 7 : '8SU', 6 : '3UB', 5 : '2MB', 4 : '1LB', 8 : '7SL'}
    return berth[n] if n == 8 else berth[n % 8]

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n =int(input())
        print(neighbour(n))
