#list
num = [10,20,30,40,50]
print(num)
num.append(60)
print(num)
num.insert(2,33)
print(num)
num.remove(50)
print(num)
num.pop()
print(num)
num.sort()
print(num)
num.reverse()
print(num)
print(len(num))

#Tuple
tuple = (13,15, 18)
print("tuple" ,tuple)

#Set
set = {4, 6, 8 , 12 , 6, 14}
print("Set", set)
set.add(10)
print(set)
set.remove(8)
print(set)

#Dictionary
student = {
    "name": "Anjali",
    "age": 22   
}
print(student)

print(student["age"])

student["city"] = "Indore"
print(student)

print(student.keys())
print(student.values())
print(student.items())

print(student.get("name"))
student.update({"age":18})
print(student)

student.pop("city")
print(student)