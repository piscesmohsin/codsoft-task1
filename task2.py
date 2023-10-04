
def add(num1,num2):
    return num1 +num2
def subtract(num1,num2):
    return num1 - num2
def multiply(num1,num2):
    return num1 * num2
def division(num1,num2):
    return  num1/num2

print("select operation")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.division")


select = int(input("select operation from 1,2,3,4:"))
num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
if select == 1:
    print(num1,"+",num2,"=",add(num1,num2))
elif select == 2:
    print(num1,"-",num2,"=",subtract(num1,num2))
elif select == 3:
    print(num1,"*",num2,"=",multiply(num1,num2))
elif select == 4:
    print(num1,"/",num2,"=",division(num1,num2))        
else:
    print("invalid input")    

