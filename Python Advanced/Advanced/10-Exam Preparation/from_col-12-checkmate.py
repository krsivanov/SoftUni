a = [input().split() for _ in range(8)]
quins = []
king = ()
winners = []
for i in range(8):
    for j in range(8):
        if a[i][j] == 'K':
            king = (i, j)
        elif a[i][j] == 'Q':
            quins.append((i, j))

points = [(-1, -1), (-1, 0), (-1, 1),
           (0, -1), (0, 1),
           (1, -1), (1, 0), (1, 1)]

for (i, j) in quins:
    for point in points:
        k = i + point[0]
        l = j + point[1]
        while 0 <= k < 8 and 0 <= l < 8:
            if a[k][l] == "K":
                winners.append((i, j))
                break
            elif a[k][l] == "Q":
                break
            k += point[0]
            l += point[1]


if not winners:
    print('The king is safe!')
else:
    [print(list(pp)) for pp in winners]
