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

# Marks 90+ → A
 #75+ → B
 #60+ → C
 #40+ → D
 #below 40 → Fail

if percent>90:
    print("A")
elif percent >75:
    print("B")
elif percent>60:
    print("C")
else:
    print("D")      

#loops
# print 1-10
for i in range (1, 11):
 print(i)
# print 1-10 even numbers
for i in range (1, 11):
    if i % 2==0:
      print(i)
# print 1-10 odd numbers
for i in range (1,11):
    if i % 2!=0:
       print(i) 
#1–10 multiplication table
for i in range(1,11):
    for j in range (1,11):
     print(i*j)
       
#1–100 , 5's multiples print
for i in range (5, 101):
    if i % 5==0:
        print(i)

#1-10 sum 
sum = 0
for i in range(1,11):
    sum = sum + i
      print(sum)
