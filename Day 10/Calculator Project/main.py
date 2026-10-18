from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    should_accumulate = True
    first_number = float(input("Enter first number: "))

    while should_accumulate:
        math_operator = input('Enter mathematical operator "+", "-","*" or "/: ')
        second_number = float(input("Enter second number: "))
        result = operations[math_operator](n1 = first_number, n2 = second_number)
        print(f"{first_number} {math_operator} {second_number} = {result}")

        want_to_continue = input(f"Want to continue with {result}? or start new calculation? 'yes' or 'no': ")
        if want_to_continue == 'yes':
            first_number = result
        else:
            print("\n" * 20)
            should_accumulate = False
            calculator()

calculator()