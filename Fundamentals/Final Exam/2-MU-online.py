rooms = input().split('|')

health = 100
total_bitcoins = 0
is_alive = True

for i in range(len(rooms)):
    room = rooms[i]
    args = room.split()
    command = args[0]
    number = int(args[1])

    if command == 'potion':
        temp = health
        health += number
        healed = number
        if health > 100:
            health = 100
            healed = 100 - temp
        print(f'You healed for {healed} hp.')
        print(f'Current health: {health} hp.')
    elif command == 'chest':
        total_bitcoins += number
        print(f'You found {number} bitcoins.')
    else:
        health -= number
        if health > 0:
            print(f'You slayed {command}.')
        else:
            print(f'You died! Killed by {command}.')
            print(f'Best room: {i+1}')
            is_alive = False
            break

if is_alive:
    print("You've made it!")
    print(f'Bitcoins: {total_bitcoins}')
    print(f'Health: {health}')
