#Faulty calculator - without function

#operation shows following faulty results
# 45*3=555, 56+9=77, 56/6=4

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

opr = input("Enter any operator(+,-,/,*): ")

equ = num1+opr+num2

if equ == "45*3":
    print(555)
elif equ == "56+9":
    print(77)
elif equ == "56/6":
    print(4)
elif opr == "+":
    print(int(num1)+int(num2))
elif opr == "-":
    print(int(num1)-int(num2))
elif opr == "*":
    print(int(num1)*int(num2))
elif opr == "/":
    print(int(num1)/int(num2))
else:
    print("please check operator")