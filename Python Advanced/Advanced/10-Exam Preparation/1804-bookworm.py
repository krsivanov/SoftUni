inital_string = [x for x in input()]
n = int(input())

matrix = []
player_pos = []
directions = {
    "up":(-1,0),
    "right": (0,1),
    "down": (1,0),
    "left": (0,-1)
}

for row in range(n):
    line = [x for x in input()]
    for col in range(n):
        if line[col]== "p":
            player_pos = [row,col]
        matrix.append(line)

m = int(input())

for _ in range(m):
    command = input()
    dir_changes = directions[command]
    
