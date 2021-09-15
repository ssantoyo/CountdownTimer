#add function
def add(x,y):
    return x+y
#subtract function
def subtract(x,y):
    return x-y
#multiply function
def multiply(x,y):
    return x*y
#divide function
def divide(x,y):
    return x/y

print("Select operation of calculation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    #Takes the input from the user
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ("1", "2", "3", "4"):
        print("Start by entering values!")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if(choice == "1"):
            print(num1, "+", num2, "=", add(num1, num2))
        if(choice == "2"):
             print(num1, "-", num2, "=", subtract(num1, num2))
        if(choice == "3"):
             print(num1, "*", num2, "=", multiply(num1, num2))
        if(choice == "4"):
             print(num1, "/", num2, "=", divide(num1, num2))
