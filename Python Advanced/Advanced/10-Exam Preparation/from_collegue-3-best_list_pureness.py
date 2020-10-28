collegue's solution


from collections import deque


def best_list_pureness(a_list, k):
    a_list = deque(a_list)
    k = int(k)
    rotations = {x: [] for x in range(k + 1)}
    for i in range(0, k + 1):
        pureness = 0
        for index, number in enumerate(a_list):
            pureness += (index * number)
        rotations[i].append(pureness)
        pureness = 0

        last = a_list.pop()
        first = a_list.appendleft(last)

    all_values = rotations.values()
    max_value = max(all_values)

    for x, y in rotations.items():
        all_values = rotations.values()
        max_value = max(all_values)
        if max_value == y:
            return (f"Best pureness {y[0]} after {x} rotations ")
            break


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
