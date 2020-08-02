username = input()

cmd_input = input()

while cmd_input != "Sign up":
    args = cmd_input.split()
    cmd = args[0]

    if cmd == 'Case':
        type = args[1]

        if type == 'lower':
            username = username.lower()
        elif type == 'upper':
            username = username.upper()

        print(username)

    elif cmd == 'Reverse':
        start_index = int(args[1])
        end_index = int(args[2])
        length = len(username)
        if start_index < 0 or start_index >= length or end_index < 0 or end_index > length:
            cmd_input = input()
            continue

        res = username[start_index:end_index + 1]
        # reversed_res = "".join(list(reversed(res)))
        reverser_res = res[::-1]
        print(reverser_res)
    elif cmd == 'Cut':
        substring = args[1]

        if substring not in username:
            print(f"The word {username} doesn't contain {substring}.")
            cmd_input = input()
            continue
        username = username.replace(substring, '')
        print(username)

    elif cmd == "Replace":
        char = args[1]
        username= username.replace(char, '*')
        print(username)

    elif cmd == "Check":
        char = args[1]

        if char in username:
            print("Valid")
        else:
            print(f"Your username must contain {char}.")

    cmd_input = input()

