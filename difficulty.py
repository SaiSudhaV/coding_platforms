def difficulty_level(A : [int]) -> str:
    return "HARD" if sum(A) > 0 else "EASY"
    
if __name__ == "__main__":
    n = int(input())
    A = list(map(int, input().split()))
    print(difficulty_level(A))
