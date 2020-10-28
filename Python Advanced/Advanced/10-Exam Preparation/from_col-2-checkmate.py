def is_valid(number, size):
    return 0 <= number < size


board = []
king_pos = None
queens_that_can_capture = []

for row in range(8):
    line = input().split()
    if "K" in line:
        king_pos = (row, line.index("K"))
    board.append(line)

directions = {
    "n": (0, -1),
    "ne": (1, -1),
    "e": (1, 0),
    "se": (1, 1),
    "s": (0, 1),
    "sw": (-1, 1),
    "w": (-1, 0),
    "nw": (-1, -1),
}

for direction in directions:
    row = king_pos[0]
    col = king_pos[1]

    row_changes = directions[direction][0]
    col_changes = directions[direction][1]

    if not is_valid(row + row_changes, 8) or not is_valid(col + col_changes, 8):
        continue

    while is_valid(row, 8) and is_valid(col, 8):
        current_cell = board[row][col]
        if current_cell == "Q":
            queens_that_can_capture.append([row, col])
            break
        else:
            row += row_changes
            col += col_changes
            continue

if len(queens_that_can_capture)==0:
    print("The king is safe!")
else:
    for x in queens_that_can_capture:
        print(x)

