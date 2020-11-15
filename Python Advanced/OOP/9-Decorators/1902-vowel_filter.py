def vowel_filter(func):
    def wrapper():
        result = func()
        vowels = {'a', 'e', 'o', 'u', 'i', 'y'}
        return [x for x in result if x in vowels]
    return wrapper




@vowel_filter
def get_letters():
    return ['a', 'b', 'c', 'd', 'e']
print(get_letters())
