first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
number_of_students = int(input())

hour_counter = 0
students_left = number_of_students
students_per_hour = first_employee+second_employee+third_employee

while students_left>=0:
    if students_left>=students_per_hour:
        hour_counter +=1
    else:
        if hour_counter <=3 :
            hour_counter +=1
        break
    if hour_counter%3==0:
        continue
    students_left -= students_per_hour



print(f'Time needed: {hour_counter}h.')