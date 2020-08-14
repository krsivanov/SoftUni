string = input()
data = input()
while data != 'Reveal':
    tokens = data.split(':|:')
    command = tokens[0]
    if command =='InsertSpace':
        index = int(tokens[1])
        string = string[:index] + ' '+ string[index:]
        print(string)

    elif command == 'Reverse':
        substring = tokens[1]
        if substring in string:
            string = string.replace(substring, '', 1)
            string += substring[::-1]
            print(string)
        else:
            print("error")
    elif command =='ChangeAll':
        substring = tokens[1]
        replacement = tokens[2]
        string = string.replace(substring,replacement)
        print(string)


    data = input()

print(f'You have a new text message: {string}')