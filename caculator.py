num1 = float(input("enter first number:"))
num2 = float(input("enter second number:"))

print("select operation")
print("1.add(+)")
print("2.substract(-)")
print("3.multiply(*)")
print("4.divide(/)")

chioce = input("enter chioce(1/2/3/4/)")

if chioce == '1':
    print(num1, "+", num2, "=", num1+num2)
elif chioce == '2':
    print(num1, "-", num2, "=", num1-num2)
elif chioce == '3':
    print(num1, "*", num2, "=", num1*num2)
elif chioce == '4':
    if num2 !=0:
        print(num1, "/", num2, "=", num1/num2)
    else:
        print("error: division by zero")
else:
    print("invalid input")
    