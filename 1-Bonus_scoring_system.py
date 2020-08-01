import math

count_of_students = int(input())
count_of_lectures = int(input())
initial_bonus = int(input())
attendances = []
bonus_points = []

if count_of_lectures == 0:
    print('Max Bonus: 0.')
    print('The student has attended 0 lectures.')
else:
    for students in range(0, count_of_students):
        x = input()
        attendances.append(x)

    attendances = [int(x) for x in attendances]

    for student in attendances:
        total_bonus = math.ceil(student / count_of_lectures * (5 + initial_bonus))
        bonus_points.append(total_bonus)


    max_bonus = int(max(bonus_points))
    max_attendances = int(max(attendances))

    print(f"Max Bonus: {max_bonus}.")
    print(f'The student has attended {max_attendances} lectures.')





# решение от форум1

import math

# students = int(input())
# lectures = int(input())
# initial_bonus = int(input())
# attendance_list = []
#
# if lectures == 0:
#     print(f'Max Bonus: 0.')
#     print(f'The student has attended 0 lectures.')
# else:
#     for i in range(1, students + 1):
#         attendances = int(input())
#         attendance_list.append(attendances)
#
#     print(f'Max Bonus: {math.ceil((max(attendance_list) / lectures) * (5 + initial_bonus))}.')
#     print(f'The student has attended {max(attendance_list)} lectures.')

#REshenie ot lekciq

# import math
# students_count = int(input())
# lectures_count = int(input())
# additional_bonus = int(input())
# current_max_bonus = 0
# student_max_attendancies = 0
#
# for i in range(students_count):
#     student_attendances = int(input())
#
#     total_bonus = student_attendances / lectures_count * (5+additional_bonus)
#
#     if total_bonus > current_max_bonus:
#         current_max_bonus = total_bonus
#         student_max_attendancies = student_attendances
#
# print(f'Max Bonus: {math.ceil(current_max_bonus)}')
# print(f'The student has attended {student_max_attendancies} lectures.')
#
