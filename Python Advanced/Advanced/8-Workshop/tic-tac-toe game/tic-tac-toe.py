class Player:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def __str__(self):
        return f"Name: {self.name}, Mark: {self.mark}"
    def __repr__(self):
        return f"Name: {self.name}, Mark: {self.mark}"

def print_board(board):
    for row in board:
        values = []
        for cell in row:
            if cell is None:
                values.append(' ')
            else:
                values.append(cell)
        values_str = " | ".join(values)
        print(f'| {values_str} |')

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
    BOARD_SIZE = 3
    player_one = setup_player()
    player_two = setup_player("0" if player_one.mark == "X" else "0")
    board = setup_board(BOARD_SIZE)


    return (board,player_one,player_two)

def print_welcome(player):
    print("This is the numeration of the board:")
    print("| 1 | 2 | 3 |")
    print("| 4 | 5 | 6 |")
    print("| 7 | 8 | 9 |")
    print(f"{player.name} starts first!")


def game_loop():
    while True:
        pass

def start_game():
    (board, *players) = setup()
    print_welcome(players[0])


start_game()