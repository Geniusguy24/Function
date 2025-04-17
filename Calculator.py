
operation = input("What operation would you like to perform? (Add, Subtract, Multiply, Divide)")

def add(P, Q):
    result = P + Q
    return result
def subtract(P, Q):
    result = P - Q
    return result
def multiply(P, Q):
    result = P * Q
    return result
def divide(P, Q):
    result = P / Q
    return result

P = int(input("Please Enter the first number!"))

Q = int(input("Please Enter the second number!"))

if operation == ("add" or "Add"):
    print(add(P,Q))
elif operation == ("subtract" or "Subtract"):
    print(subtract(P, Q))
elif operation == ("Multiply" or "multiply"):
    print(multiply(P, Q))
elif operation == ("Divide" or "divide"):
    print(divide(P, Q))
else:
    print("Invalid Input! Please try again")

