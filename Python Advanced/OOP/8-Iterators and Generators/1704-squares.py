def squares(n):
    current_num = 1
    while current_num <= n:
        yield current_num ** 2
        current_num += 1

class squares_iter:
    def __init__(self,n):
        self.n = n
        self.current_num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num <= self.n:
            temp = self.current_num
            self.current_num += 1
            return temp**2
        raise StopIteration()


print(list(squares(5)))
