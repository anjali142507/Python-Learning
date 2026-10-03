#print name, age, city
name = "Anjali"
age = 22
city = "Indore"

print(name, age, city)

#Take to number and perform addition, subtraction, multiplication and division

num1 = 10
num2 = 5

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

#Take marks as a input from user and calculate percentage type output

marks = float(input("Enter your marks:"))

total_marks = 500
percent = (marks/total_marks) * 100
print(percent)


#If else - Number is even or odd

number = int(input("Enter a number:"))
if number % 2 == 0:
    print("even")
else:
    print("odd")

# Number is pos, neg or zero
number2 = int(input("Enter a number"))
if(number2 > 0):
    print("positive")
elif(number2 < 0):
    print("negative")
else:
    print("zero")    

#age is 18+ or not
if(age > 18):
    print("Yes")
else:
    print("No")    

