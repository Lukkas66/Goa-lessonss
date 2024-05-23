num_of_marks = int(input("Enter the number of marks: "))
marks = []
for i in range(num_of_marks):
    mark = float(input("Enter mark {}: ".format(i+1)))
    marks.append(mark)

total_marks = sum(marks)
mean = total_marks / num_of_marks

# Print the arithmetic mean
print("The arithmetic mean of marks:", mean)
