def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y!=0:
        return x/y
    else:
        return "Error! Division by zero."
def main():
    while True:
        print("Simple Calculator")
        print("1.Add 2.Subtract 3.Multiply 4.Divide 5.Exit")
        choice=input("Enter choice 1/2/3/4/5: ")
        if choice=='5':
            print("Exit")
            break
        if choice in '1234':
            num1=float(input("Enter first number: "))
            num2=float(input("Enter second number: "))
            if choice=='1':
                print("The result of num1+num2 is", add(num1,num2))
            elif choice=='2':
                print("The result of num1-num2 is", subtract(num1,num2))
            elif choice=='3':
                print("The result of num1*num2 is", multiply(num1,num2))
            elif choice=='4':
                result=divide(num1,num2)
                if result=="Error! Division by zero.":
                    print(result)
                else:
                    print("The result of num1/num2 is", result)
        else:
            print("Invalid input. Please enter a valid choice.")
main()
