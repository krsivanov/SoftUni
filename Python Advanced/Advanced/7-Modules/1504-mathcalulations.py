from math_operations import perform_operation

tokens = input().split()
x =tokens[0]
operation = tokens[1]
y = tokens[2]
print(perform_operation(x,y,operation))