# create operations as functions
def add(n1, n2):
    """adds number 1 to number 2"""
    return n1 + n2

def sub(n1, n2):
    """Subtracts number 2 from number 1"""
    return n1 - n2

def mult(n1, n2):
    """Multiply Number 1 by Number 2"""
    return n1 * n2

def dev(n1, n2):
    """Devide Number 1 by Number 2"""
    return n1 / n2

#creatye a dictionary for all operations
operations = {
    "+": add,
    "-": sub, 
     "*": mult, 
     "/": dev
 }

#create a function to calculate the operation
def calc():
    """Asks for numbers (number 1 and number 2), operation type, shows the result, asks if you want to proceed with other calculations for the result, or start new"""
    should_proceed = True
    n1 = float(input("what is the number?"))
    while should_proceed:   
        for symbol in operations:
            print(symbol)
        operation = input("what operation do you need? Please type +, -, * or /: \n")
        n2 = float(input("What is the second number?"))
        result = operations[operation](n1, n2)
        print(f"{n1} {operation} {n2} = {result}")
        proceed = input(f"Type 'y' to continue calculation with {result}, or type 'n' to start a new calculation\n").lower()
        if proceed == "y":
            n1 = result
        else:
            should_proceed = False
            print("\n" * 20)
            calc()
calc()