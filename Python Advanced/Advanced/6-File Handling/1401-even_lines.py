with open("text.txt", "w") as file:
    for idx, line in enumerate(file):
        if idx%2 == 0:
            for el in "-,.!?":
                line = line.replace(el, @)
            words = reversed(line.split())
            print(' '.join(words))
