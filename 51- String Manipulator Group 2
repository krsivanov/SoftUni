string = input()
manipulated_string =string
while True:
  tokens = input().split()
  command = tokens[0]

  if command == "Done":
    break
  
  elif command == "Change":
    char = tokens[1]
    replacement=tokens[2]
    manipulated_string = string.replace(char,replacement)
    print(manipulated_string)
    
  elif command == "Includes":
    included_string = tokens[1]
    if included_string in manipulated_string:
      print(True)
    else:
      print(False)
  
  elif command == "End":
    end_string = tokens[1]
    if end_string==manipulated_string[-len(end_string):]:

      print(True)
    else:
      print(False)


  elif command== "Uppercase":
    manipulated_string = manipulated_string.upper()
    print(manipulated_string)

  elif command=="FindIndex":
    char = tokens[1]
    index = manipulated_string.find(char)
    if index != -1:
      print(index)
    else:
      continue

  elif command=="Cut":
    start_index = int(tokens[1])
    length = int(tokens[2])
    manipulated_string = manipulated_string[start_index:start_index+length]
    print(manipulated_string)

