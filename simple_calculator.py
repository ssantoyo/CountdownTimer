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