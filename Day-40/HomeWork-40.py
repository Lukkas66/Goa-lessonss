numbers = input("Enter numbers separated by spaces: ").split()

numbers = [int(number) for number in numbers]

two_digit_count = sum(10 <= abs(number) < 100 for number in numbers)

print(f"There are {two_digit_count} two-digit numbers in the list.")
