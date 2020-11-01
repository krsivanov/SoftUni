from random import randint

class RandomList(list):
    def get_random_element(self):
        index_to_remove = randint(0, len(self))
        return self.pop(index_to_remove)
