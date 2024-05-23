grade = int(input("Enter the grade obtained in the school test: "))

if grade == 10:
    print("Your son is good student.")
elif grade == 8 or grade == 9:
    print("For now you son is gets very bad grades .")
elif grade == 5:
    print("Your son is not studying anything.")
elif grade < 5:
    print("Bad news your son is kicked from school.")
else:
    print("Invalid grade entered.")
