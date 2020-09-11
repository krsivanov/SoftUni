countries = input().split(', ')
capitals = input().split(', ')
result = {pair[0]: pair[1] for pair in zip(countries, capitals)}

[print(f'{key} -> {value}') for key,value in result.items()]
