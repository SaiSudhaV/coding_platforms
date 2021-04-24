def decimal_binary(num):
	binary = bin(num)
	return str(binary)[2:]
def get_input(n):
	input_list = []
	for i in range(n):
		input_list[i] = int(input())
	return input_list
def passing_elements(input_list, n):
	for i in range(n):
		decimal_binary(input_list[i])
