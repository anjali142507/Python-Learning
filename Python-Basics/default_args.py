def greet(name="Anjali"): #default value = Anjali
    print("Hello" , name)
greet() #No argument that's why anjali is used
greet("Rahul") #here we give our value


#write a function welcome & set its default city = "Indore", 
# call welcome() & print Welcome to Indore 
# call welcome("Bhopal") & print Welcome to Bhopal


def welcome(city = "Indore"):
    print("Welcome to" , city)

welcome()
welcome("Bhopal")