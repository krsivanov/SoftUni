friend_list =  input().split(', ')
input_command = input()
blacklisted = 0
lost = 0


while input_command != 'Report':
    args = input_command.split()
    command = args[0]
    second_index = args[1]


    if command == "Blacklist":
        if second_index in friend_list:
            index = friend_list.index(second_index)
            friend_list[index]='Blacklisted '
            print(f'{second_index} was blacklisted.')
            blacklisted +=1
        elif second_index not in friend_list:
            print(f'{second_index} was not found.')
    elif command == "Error":
        if second_index in friend_list:
            if second_index != 'Blacklisted' or second_index != 'Lost':
                index = friend_list.index(second_index)
                friend_list[index]='Lost'
                lost += 1
                print(f'{second_index} was lost due to an error.')
    elif command == 'Change':
        pass

    input_command= input()

print(f'Blacklisted names: {blacklisted}')
print(f'Lost names: {lost}')
print(friend_list)