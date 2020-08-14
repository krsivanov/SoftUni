import re

pattern = r'^(.+)>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^<>]{3})<(\1)$'

n=int(input())

for i in range(n):
    password = input()

    match = re.fullmatch(pattern,password)

    if match is None:
        print("Try another password!")
        continue

    group_one = match[2]
    group_two = match[3]
    group_three = match[4]
    group_four = match[5]

    encrypted_pass = group_one +group_two + group_three+group_four

    print(f'Password: {encrypted_pass}')