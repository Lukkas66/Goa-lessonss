numbers_list = [1, 2, 3, 4, 5]

reversed_list = []

for i in range(len(numbers_list) - 1, -1, -1):
    reversed_list.append(numbers_list[i])

print("Original list:", numbers_list)
print("Reversed list:", reversed_list)
