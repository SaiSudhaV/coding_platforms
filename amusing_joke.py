# your code goes here

def can_permute(s1, s2, s):
    tem1, tem2 = list(s1 + s2), list(s)
    return "YES" if sorted(tem1) == sorted(tem2) else "NO"

if __name__ == "__main__":
    guest_name = input()
    host_name = input()
    pile_of_letters = input()
    print(can_permute(guest_name, host_name, pile_of_letters))