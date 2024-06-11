even_numbers = []
odd_numbers = []

def is_even(number):
    return number % 2 == 0

print("Please enter 10 even numbers:")
while len(even_numbers) < 10:
    try:
        num = int(input(f"Enter even number {len(even_numbers) + 1}: "))
        if is_even(num):
            even_numbers.append(num)
        else:
            print(f"{num} is not an even number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

print("Please enter 10 odd numbers:")
while len(odd_numbers) < 10:
    try:
        num = int(input(f"Enter odd number {len(odd_numbers) + 1}: "))
        if not is_even(num):
            odd_numbers.append(num)
        else:
            print(f"{num} is not an odd number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
    