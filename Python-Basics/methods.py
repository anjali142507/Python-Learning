#Method
class Calculator:
    def add(self, a , b):
        return a+b
    
obj = Calculator()
print(obj.add(10,2))

#Built in function and Built in method

nums = [10 ,20 ,30]

print(len(nums)) #function

nums.append(40) #method

print(nums)