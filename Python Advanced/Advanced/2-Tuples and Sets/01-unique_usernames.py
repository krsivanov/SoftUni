n = int(input())
unique_usernames = set()

for _ in range(n):
  username = input()
  unique_usernames.add(username)

for username in unique_usernames:
  print(username)

#print('\n'.join(unique_usernames))

#[print(x) for x in unique_usernames]
