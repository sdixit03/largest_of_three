print("Enter first number: ")
num1=int(input())
print("Enter second number: ")
num2=int(input())
print("Enter third number: ")
num3=int(input())
if num1>=num2 and num1>=num3:
    print(num1)
elif num2>=num1 and num2>=num3:
    print(num2)
else:
    print(num3)
