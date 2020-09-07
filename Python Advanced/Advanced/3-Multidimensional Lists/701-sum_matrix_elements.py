(rows_count, columnst_count) = [int(x) for x in input().split(', ')]
matrix = []

for row_index in range(rows_count):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)

total_sum = 0
for row in matrix:
    total_sum += sum(row)


print(total_sum)
print(matrix)
