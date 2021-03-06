number = int(input())
plants_rarity = {}
plants_rating = {}
for plant in range(number):
    new_plants = input().split("<->")
    if new_plants[0] not in plants_rarity.keys():
        plants_rarity[new_plants[0]] = int(new_plants[1])
    else:
        plants_rarity[new_plants[0]] = int(new_plants[1])
    if new_plants[0] not in plants_rating.keys():
        plants_rating[new_plants[0]] = []
    else:
        plants_rating[new_plants[0]] = []
command = input().split(": ")
while command[0] != "Exhibition":
    plants_for_changing = command[1].split(" - ")
    plants_name = plants_for_changing[0]
    if command[0] == "Rate":
        rating = int(plants_for_changing[1])
        if plants_name in plants_rating.keys():
            plants_rating[plants_name].append(rating)
        else:
            print("error")
    elif command[0] == "Update":
        rarity = int(plants_for_changing[1])
        if plants_name in plants_rarity.keys():
            plants_rarity[plants_name] = rarity
        else:
            print("error")
    elif command[0] == "Reset":
        if plants_name in plants_rating.keys():
            plants_rating[plants_name] = []
        else:
            print("error")
    command = input().split(": ")
sorted_plants = []
for key, value in plants_rating.items():
    sorted_plants.append([[key], [int(s) for s in value], plants_rarity[key]])
sorted_plants = list(reversed(sorted(sorted_plants, key=lambda x: (x[2], x[1]))))
print("Plants for the exhibition:")
for items in sorted_plants:
    plant_name = items[0][0]
    rarity = items[2]
    sum = 0
    for i in items[1]:
        sum += int(i)
    if sum != 0:
        middle_rating = sum / len(items[1])
    else:
        middle_rating = 0
    print(f"- {plant_name}; Rarity: {rarity}; Rating: {middle_rating:.2f}")



