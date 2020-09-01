names = set()
n = int(input())

for _ in range(n):
  names.add(input())
#[names.add(input()) for _ in range(n)]

for name in names:
  print(name)
#[print(name) for name in names]

