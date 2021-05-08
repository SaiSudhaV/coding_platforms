kings_list = [int(i) for i in input().split(',')]
first_term = kings_list[0]
second_term = kings_list[1]
print(True) if ((kings_list[2] == first_term - 1 or kings_list[2] == first_term + 1 or kings_list[2] == first_term) and (kings_list[3] == second_term - 1 or kings_list[3] == second_term + 1 or kings_list[3] == second_term)) else print(False) 
