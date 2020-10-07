from collections import deque

males = [int(x) for x in input().split()]
females = deque([int(x) for x in input().split()])
matches = 0

while males and females:
    male = males[-1]
    female = females[0]

    if male == 0:
        males.pop()
        continue
    elif females==0:
        females.popleft()
        continue
    elif female==male:
        females.popleft()
        males.pop()
        matches += 1
