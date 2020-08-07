emails_data = {}
counter_of_users = 0

while True:
    user_input = input()

    if user_input == "Statistics":
        break

    args = user_input.split("->")
    command = args[0]
    username = args[1]

    if command == 'Add':
        if username in emails_data:
            print(f"{username} is already registered")
            continue

        emails_data[username] = []
        counter_of_users += 1

    elif command == "Send":
        if username not in emails_data:
            emails_data[username] = []
            counter_of_users += 1

        email = args[2]
        emails_data[username].append(email)

    elif command == "Delete":
        if username not in emails_data:
            print(f"{username} not found!")
            continue

        emails_data.pop(username)
        counter_of_users -=1
print(f'Users count: {counter_of_users}')
sorted_emails = dict(sorted(emails_data.items(), key= lambda k: (-len(k[1]),k[0])))

for (key,value) in sorted_emails.items():
  print(f'{key}')
  for mail in value:
    print(f' - {mail}')



