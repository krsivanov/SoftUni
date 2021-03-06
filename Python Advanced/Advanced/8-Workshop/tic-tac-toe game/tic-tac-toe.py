BOARD_SIZE = 3


class Player:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def __str__(self):
        return f"Name: {self.name}, Mark: {self.mark}"
    def __repr__(self):
        return f"Name: {self.name}, Mark: {self.mark}"

# def print_board(board):
#     for row in board:
#         values = []
#         for cell in row:
#             if cell is None:
#                 values.append(' ')
#             else:
#                 values.append(cell)
#         values_str = " | ".join(values)
#         print(f'| {values_str} |')

def setup_board(size):
    return [[None]*size for _ in range(size)]     

def setup_player(mark = None):
    name = input("Name: ")
    if not mark:
        mark = input("Mark: ")
    else:
        print(f"Mark: {mark}")
    return Player(name, mark)

def setup():
    player_one = setup_player()
    player_two = setup_player("0" if player_one.mark == "X" else "0")
    board = setup_board(BOARD_SIZE)


    return (board,player_one,player_two)

# def print_welcome(player):
#     print("This is the numeration of the board:")
#     print("| 1 | 2 | 3 |")
#     print("| 4 | 5 | 6 |")
#     print("| 7 | 8 | 9 |")
#     print(f"{player.name} starts first!")

def get_position(player):
    position = int(input(f"{player.name} chooses a free position[1-9]: "))
    row = (position - 1)// BOARD_SIZE
    column = (position -1) % BOARD_SIZE

    return (row,column)

def place_mark(board,player):
    (row, column) = get_position(player)
    board[row][column] = player.mark

def all_single_value(ll,value):
    for v in ll:
        if v!=value:
            return False
        return True

def check_game_over(board, player):
    rows = board
    columns = [[board[i][j] for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]
    diagonals = [
        [board[i][i] for i in range(BOARD_SIZE)],
        [board[i][BOARD_SIZE-i-1] for i in range(BOARD_SIZE)]
    ]

    row_checks = [all_single_value(row, player.mark) for row in rows]
    column_checks = [all_single_value(column, player.mark) for column in columns]
    diagonal_chekcs = [all_single_value(diagonal, player.mark) for diagonal in diagonals]
    
    all_checks = [
        *row_checks,
        *column_checks,
        *diagonal_chekcs
    ]
    return any(all_checks)

# def print_game_over(board,player):
#     print_board(board)
#     print(f'{player.name} won!')

def game_loop(board, players):
    current_player, next_player = players
    
    while True:
        print_board(board)
        place_mark(board,current_player)
        if check_game_over(board,current_player):
            print_game_over(board, current_player)
            break
        current_player, next_player = next_player, current_player


def start_game():
    (board, *players) = setup()
    print_welcome(players[0])
    game_loop(board,players)

start_game()
