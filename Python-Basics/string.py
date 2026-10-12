#Take string input from user and print len of string , uppercase , lowercase 
s = input("Enter a string:")
length = len(s)
upr = s.upper()
lwr = s.lower()

print(length)
print(upr)
print(lwr)

#Reverse a string
print(s[::-1])

#Check if string is palindrome or not
rev = s[::-1]
if s == rev:
    print("palindrome")
else:
    print("not palindrome")