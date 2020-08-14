string = input()
raw_pass = ''

while True:
    command = input()
    if command == 'Done':
        break
    tokens = command.split()
    if tokens[0] == 'TakeOdd':
        for i, s in enumerate(string):
            if i % 2 != 0:
                raw_pass += s
        string = raw_pass
    elif tokens[0] == 'Cut':
        index = int(tokens[1])
        length = int(tokens[2])
        substring = string[index:index+length]
        string = string.replace(substring, '', 1)
        # raw_pass = string
    elif tokens[0] == 'Substitute':
        substring = tokens[1]
        substitute = tokens[2]
        if substring in string:
            string = string.replace(substring, substitute)
        else:
            print('Nothing to replace!')
            continue
    print(string)

print(f'Your password is: {string}')
