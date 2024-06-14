#price = int(input("sheikvanet produqciss fasi: "))
#discount = int(input("ra aris misi fasi?: "))
#num = (price * discount) / 100
#print("price - num")  


odd_numbers = []
even_numbers = []

def append_number(number):
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

user_input = input("Enter a number: ")

while user_input.lower() != 'q':
    try:
        number = int(user_input)            
        append_number(number)
        print(f"Odd numbers: {odd_numbers}")
        print(f"Even numbers: {even_numbers}")
    except ValueError:
        print("Please enter a valid number.")
    
    user_input = input("Enter a number): ")

print("Final lists:")
print(f"Odd numbers: {odd_numbers}")
print(f"Even numbers: {even_numbers}")
