numbers = []
greater_than_100 = []
less_than_or_equal_to_100 = []

for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

for num in numbers:
    if num > 100:
        greater_than_100.append(num)
    else:
        less_than_or_equal_to_100.append(num)

print("რიცხვები რომლებიც მეტია 100ზე:", greater_than_100)
print("რიცხვები რომლებიც ნაკლებია 100ზე:", less_than_or_equal_to_100)
