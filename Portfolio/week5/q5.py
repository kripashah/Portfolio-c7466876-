
#write a program to find largest number using lambda
largest=lambda x, y : x if x>y else y

num1=float(input("Enter the first num:"))
num2=float(input("Enter the second num:"))

largest_number=largest(num1,num2)
print("The largest num is:",largest_number)

#write a program to read marks for 5 subject of a student.Your program should give the average result using
#lambda expression.