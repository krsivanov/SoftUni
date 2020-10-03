presents_count = int(input())
n = int(input())

matrix = []
for row in range(n):
    line = input().split()
    for col in range(n):
        if line[col] == "S":
            santa_pos = [row, col]
        matrix.append(line)

while True:
    line = input()
    if line == "Christmas morning":
        break
