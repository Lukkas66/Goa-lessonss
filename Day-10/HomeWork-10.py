number1 = int(input("number 1: "))
number2 = int(input("number 2: "))
number3 = int(input("number 3: "))

answer1 = number1 < number2
answer2 = number2 > number3
answer3 = number1 > number3

print(answer1 and answer2)
print(answer2 or answer3)
print(answer3 and answer1)