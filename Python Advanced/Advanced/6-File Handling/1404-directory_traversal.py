import os

path = input()
result_dict = {}

for root, dirs, files in os.walk(path):
    if root.count(os.path.sep) > 1:
        continue
    for file in files:
        extension = file.split(".")[1]
        if extension not in result_dict:
            result_dict[extension] = []
        result_dict[extension].append(file)
        
print(result_dict)
