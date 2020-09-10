def read_matrix():
    rows_count = int(input())
    return [map(int, input().split(', ')) for _ in range(rows_count)]

matrix = read_matrix()
flattened = [num
             for sublist in matrix
             for num in sublist]

print(flattened)




