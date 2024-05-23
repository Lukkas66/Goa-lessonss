score = int(input("Enter the score obtained in the test: "))

if score >= 90 and score < 100:
    print("Congratulations! You will be fully funded for your studies.")
elif score >= 70 and score < 80:
    print("You will be financed with 1500 GEL.")
elif score >= 40 and score < 70:
    print("You will be financed with 500 GEL.")
elif score < 40:
    print("Your study process will not be financed.")
else:
    print("Invalid score entered.")
