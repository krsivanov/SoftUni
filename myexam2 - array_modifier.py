integers = list(map(int, input().split()))
input_command = input()

while input_command != 'end':
    arg = input_command.split()
    command = arg[0]

    if command == 'swap':
        index1 = int(arg[1])
        index2 = int(arg[2])
        swapped_number = integers[index1]
        integers[index1] = integers[index2]
        integers[index2]=swapped_number
    elif command == 'multiply':
        index1 = int(arg[1])
        index2 = int(arg[2])
        integers[index1]= integers[index1]*integers[index2]
    elif command == 'decrease':
        for i in range(len(integers)):
            integers[i] -=1

    input_command = input()

print(*integers, sep=", ")
