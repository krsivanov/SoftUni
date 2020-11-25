# class CustomListIndexException(Exception):
#     pass
#
# class CustomListTypeException(Exception):
#     pass
# class CustomListSumException(Exception):
#     pass
from collections.abc import Iterable
from workshop_custom_list.errors import CustomListIndexException, CustomListTypeException, CustomListSumException


def is_index_integer(index):
    if not isinstance(index, int):
        raise CustomListTypeException(f'Index must be of type string it was {type(index)}')
    return True


class CustomList:
    def __init__(self, *args):
        self.sequence = [el for el in args]

    def append(self, value):
        self.sequence += [value]
        return self.sequence

    def remove(self, index):
        try:
            value = self.sequence[index]
            del self.sequence[index]
            return value
        except IndexError as ex:
            raise CustomListIndexException(f"MyCustom list does not "
                                           f"found element on this index - {index}\n"
                                           f"Original exception was - {str(ex)}")

        except TypeError:
            raise CustomListTypeException(f"Index must be of type string it was {type(index)}")

    def get(self, index):
        try:
            return self.sequence[index]
        except IndexError as ex:
            raise CustomListIndexException(f"MyCustom list does not "
                                           f"found element on this index - {index}\n"
                                           f"Original exception was - {str(ex)}")
        except TypeError as ex:
            raise CustomListTypeException(f'Index argument does not match the supported type. '
                                          f'Should be integer it was {type(index)}')

    def extend(self, iterable):
        if not isinstance(iterable, Iterable):
            raise CustomListTypeException(f"The argument should be iterable.")
        self.sequence = self.sequence + list(iterable)
        return self.sequence

    def insert(self, index, value):
        if not isinstance(index, int):
            raise CustomListTypeException(
                f"Index argument does not match the supported type. Should be integer it was {type(index)}")
        self.sequence = self.sequence[0:index] + [value] + self.sequence[index:]
        return self.sequence

    def pop(self):
        try:
            value = self.sequence[-1]
            del self.sequence[-1]
            return value
        except IndexError as ex:
            raise CustomListIndexException(f"MyCustomList does not contain elements")

    def clear(self):
        self.sequence = []

    def index(self, value):
        for index in range(len(self.sequence)):
            if self.sequence[index] == value:
                return index
        return -1

    def count(self, value):
        counter = 0
        for el in self.sequence:
            if el == value:
                counter += 1
        return counter

    def reverse(self):
        return self.sequence[::-1]

    def copy(self):
        copy_list = [el for el in self.sequence]
        return CustomList(*copy_list)

    def __str__(self):
        return f"{' ; '.join([str(el) for el in self.sequence])}"

    def size(self):
        counter = 0
        for el in self.sequence:
            counter += 1
        return counter
        # return len(self.sequence)

    def add_first(self, value):
        self.sequence = [value] + self.sequence

    def dictionize(self):
        custom_dict = {}
        for index in range(0, len(self.sequence), 2):
            try:
                custom_dict[self.sequence[index]] = self.sequence[index + 1]
            except IndexError:
                custom_dict[self.sequence[index]] = ' '
        return custom_dict

    def move(self, amount):
        if len(self.sequence)==0:
            return []
        self.sequence = self.sequence[amount:] + self.sequence[0:amount]
        return self.sequence

    def sum(self):
        result = 0
        for el in self.sequence:
            if isinstance(el, int) or isinstance(el, float):
                result += el
                continue
            try:
                result += len(el)
            except TypeError as ex:
                raise CustomListSumException(f"Please provide a len method to custom objects"
                                             f" if you want to sum elements.\n Original exception was - {str(ex)}")
        return result

    def overbound(self):
        max_number = float('-inf')
        element = None
        for el in self.sequence:
            if not isinstance(el, int) and not isinstance(el, float):
                num = len(el)
            else:
                num = el
            if max_number < num:
                max_number = num
                element = el
        return self.index(element)

    def underbound(self):
        min_number = float('inf')
        element = None
        for el in self.sequence:
            if not isinstance(el, int) and not isinstance(el, float):
                num = len(el)
            else:
                num = el
            if min_number > num:
                min_number = num
                element = el
        return self.index(element)


my_custom_list = CustomList(4, 5, 3, 4, 5, 5, -5, 'asdf')
my_custom_list.append(100)
my_list = CustomList(1, -2, 'asdfe', 3)
print(my_custom_list)
print(my_custom_list.remove(1))
print(my_custom_list.extend([6, 8, 33]))
print(my_custom_list.insert(4, 345))
print(my_custom_list.pop())
print(my_custom_list.index("asd"))
print(my_custom_list.count(5))
print(my_custom_list.reverse())
print(my_custom_list)
print(my_custom_list.dictionize())
print(my_custom_list.move(2))
print(my_custom_list.sum())
print(my_custom_list.overbound())
print((my_list.overbound()))
print(my_custom_list.underbound())
print((my_list.underbound()))
