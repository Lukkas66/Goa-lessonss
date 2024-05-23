user_age = int(input("How old are you? "))

parents_age = int(input("How old are your parents? "))

if user_age > parents_age:
    print("You are older than your parents.")
elif user_age < parents_age:
    print("You are younger than your parents.")
else:
    print("You and your parents are the same age.")
