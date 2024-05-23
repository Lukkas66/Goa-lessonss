def main():
    # Getting user input
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    age = int(input("Enter your age: "))
    address = input("Enter your address: ")

    # Creating the big sentence
    user_info = f"{first_name} {last_name}, {age} years old, from {address}."

    # Printing user information as one big sentence
    print("\nUser Information:")
    print(user_info)

    # Calculating age after 20 years
    age_in_20_years = age + 20
    print("In 20 years, you will be {} years old.".format(age_in_20_years))

if __name__ == "__main__":
    main()