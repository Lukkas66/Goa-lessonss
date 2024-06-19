numbers_list = []       
even = []
odd = []

for i in range(10):
    numbers = int(input("Enter a number: "))
    numbers_list.append(numbers)

for i in range(len(numbers_list)):
    if numbers_list[i] % 2 == 0:
        even.append(numbers_list[i])
    else:
        odd.append(numbers_list[i])

print("Even numbers:", even)
print("Odd numbers:", odd)
