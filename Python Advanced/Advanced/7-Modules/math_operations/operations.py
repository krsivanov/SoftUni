def perform_sum(x, y):
    return x + y


def perform_substraction(x, y):
    return x - y


def perform_multiplication(x, y):
    return x * y


def perform_division(x, y):
    return x / y


def perform_gradation(x, y):
    return x ** y


def perform_operation(x, y, operation):
    if operation == "+":
        return perform_sum(x, y)
    elif operation == '-':
        return perform_substraction(x, y)
    elif operation == '*':
        return perform_multiplication(x, y)
    elif operation == "/":
        return perform_division(x, y)
    elif operation == '^':
        return perform_gradation(x, y)
