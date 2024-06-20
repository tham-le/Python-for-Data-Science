from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))  # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # output: 0
print(count_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 5))  # output: 1
print(count_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 10))  # output: 0
print(count_in_list([], 10))  # output: 0
