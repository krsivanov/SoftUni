# def set_create(length):
#   n=set()
#   for _ in range(length):
#     number = int(input)
#     n.add(number)
  
#   return n


tokens = list(map(int, input().split()))
n_length = tokens[0]
m_length = tokens[1]

n = set()
m=set()

for _ in range(n_length):
  number = int(input())
  n.add(number)

for _ in range(m_length):
  number = int(input())
  m.add(number)


#intersection = n & m
intersection = n.intersection(m)

for number in intersection:
  print(number)
