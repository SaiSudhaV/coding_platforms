Stack = []

def push(n):
    Stack.append(n)
    
def pop_ele():
    top = len(Stack)
    return Stack.pop(top - 1) if Stack else "Empty"

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        s = input()
        if s == "pop":
            print(pop_ele())
        else:
            push(int(s.split()[1]))