items = input().split(", ")
input_command = input()

while input_command != "Craft!":
    args = input_command.split(" - ")
    command = args[0]
    second_arg = args[1]

    if command == "Collect":
        # if second_arg in items:
        #     input_command = input()
        #     continue
        # items.append(second_arg)
        if second_arg not in items:
            items.append(second_arg)

    elif command == "Drop":
        # if second_arg not in items:
        #     input_command= input()
        #     continue
        # items.remove(second_arg)
        if second_arg in items:
            items.remove(second_arg)
    elif command== 'Combine Items':
        second_arg_tokens = second_arg.split(":")
        old_item = second_arg_tokens[0]
        new_iem = second_arg_tokens[1]

        if old_item in items:
            old_item_index = items.index(old_item)
            items.insert(old_item_index+1, new_iem)
    elif command == "Renew":
        if second_arg in items:
            items.remove(second_arg)
            items.append(second_arg)


    input_command = input()


print(', '.join(items))
