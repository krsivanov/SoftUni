def squares(n):
    current_num = 1
    while current_num <= 5:
        yield current_num ** 2
        current_num += 1




print(list(squares(5)))
