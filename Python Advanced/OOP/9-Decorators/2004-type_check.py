def type_check(type):
    def decorator(func):
        def wrapper(n):
            if isinstance(n, type):
                return func(n)
            return "Bad Type"

        return wrapper

    return decorator


class type_check_cls:
    def __init__(self, type_param):
        self._type_param = type_param

    def __call__(self,func):
        def wrapper(n):
            if isinstance(n,self._type_param):
                return func(n)
            return "Bad Type"
        return wrapper

@type_check_cls(int)
def times2(num):
    return num * 2


print(times2(2))


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
