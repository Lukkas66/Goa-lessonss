mother_age = int(input("Enter the mother's age: "))
father_age = int(input("Enter the father's age: "))

if mother_age > father_age:
    print("The mother is older than the father.")
elif father_age > mother_age:
    print("The father is older than the mother.")
else:
    print("The mother and father are the same age.")
