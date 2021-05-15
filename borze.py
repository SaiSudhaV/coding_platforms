# your code goes here

def decode(s):
    if '--' in s:
        s = s.replace('--', '2')
    if '-.' in s:
        s = s.replace('-.', '1')
    if '.' in s:
        s = s.replace('.', '0')
    return s
    
if __name__ == "__main__":
    s = input()
    print(decode(s))