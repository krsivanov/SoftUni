string = input()

while True:
    command = input()
    if command == 'End':
        break
    args = command.split()
    action = args[0]

    if action == 'Translate':
        char = args[1]
        replacement = args[2]
        string = string.replace(char, replacement)
        print(string)
    elif action == 'Includes':
        inclusion = args[1]
        if inclusion in string:
            print('True')
        else:
            print('False')
    elif action == 'Start':
        start = args[1]
        print(string.startswith(start, 0, len(start)))
    elif action == 'Lowercase':
        string = string.lower()
        print(string)
    elif action == 'FindIndex':
        char = args[1]
        idx = 0
        if char in string:
            for i in range(len(string) - 1, - 1, -1):
                if string[i] == char:
                    idx = i
                    break
            print(idx)
    elif action == 'Remove':
        start_idx = int(args[1])
        count = int(args[2])
        to_replace = string[start_idx:start_idx + count]
        string = string.replace(to_replace, '')
        print(string)
