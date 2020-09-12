numbers = [int(x) for x in input().split()]

def is_even(x):
    return x%2 == 0

print(list(filter(is_even,numbers)))
