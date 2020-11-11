class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.counter = start

    def __iter__(self):
        return self

    def __next__(self):
        current_num = self.counter
        self.counter += 1
        if self.counter <= self.end + 1:
            return current_num
        raise StopIteration()


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
