

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2
    
# Multiply    
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2    
    
operands = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide
}

def calculator():
    num1 = float(input("Enter first number: "))
    for key in operands:
        print(key)
    should_continue = True

    while should_continue:
        
        operation_symbol = input("Pick an operation: ")    
        num2 = float(input("What's the next number: "))
        calculation_function = operands[operation_symbol]
        answer = calculation_function(num1, num2)


        # My Long version
        # if operation_symbol == "+":
        #     answer = add(n1=num1, n2=num2)
        # elif operation_symbol == "-":
        #     answer = subtract(n1=num1, n2=num2)    
        # elif operation_symbol == "*":
        #     answer = multiply(n1=num1, n2=num2)    
        # elif operation_symbol == "/":
        #     answer = divide(n1=num1, n2=num2)    
            
        print(f"{num1} {operation_symbol} {num2} = {answer}")


        if input(f"Type 'y' to continue calculating {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else: 
            should_continue = False
            calculator()

calculator()


