from collections import deque

boxes = [int(x) for x in input().split()]
magics =deque([int(x) for x in input().split()])

toys = {150: "Doll", 250: "Wooden train", 300: "Teddy bear", 400: "Bicycle"}

crafted = {"Doll":0, "Wooden train":0, "Teddy bear":0, "Bicycle":0}
while boxes and magics:
    box = boxes.pop()
    magic = magics.popleft()

    total = box * magic

    if total in toys:
        toy = toys[total]
        crafted[toy] += 1
    
    elif total < 0:
        summed = box + magic
        boxes.append(summed)
    
    elif 
