n = int(input())

matrix = []

for _ in range(n):
    line = [int(x) for x in input().split()]
    matrix.append(line)

primary_diagonal_sum = 0
secondary_diagonal_sum = 0
for row in range(n):
    primary_diagonal_sum += matrix[row][row]
    secondary_diagonal_sum += matrix[row][n-row-1]

print(abs(primary_diagonal_sum-secondary_diagonal_sum))
