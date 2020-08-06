email = input()

while True:
  command = input()

  if command == 'Complete':
    break

  elif command == "Make Upper":
    email=email.upper()
    print(email)

  elif command == 'Make Lower':
    email = email.lower()
    print(email)

  elif command[:9] == 'GetDomain':
    args = command.split()
    count = int(args[1])
    index = abs(count-len(email))
    print(email[index:])

  elif command == "GetUsername":
    if "@" not in email:
      print(f"The email {email} doesn't contain the @ symbol.")
    index = 0
    i=0
    for i in range(len(email)):
      if email[i]=='@':
        index = i
    print(email[:index])
  
  elif command[:7] == 'Replace':
    args=command.split()
    char = args[1]
    email= email.replace(char,"-")
    print(email)
  elif command == "Encrypt":
    for i in range(len(email)):
      print(ord(email[i]),end=" ")
    print()
