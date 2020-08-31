def input_to_list(lines_count):
  return [input() for _ in range(lines_count)]
#  input_lines = []
#  for _ in range(lines_count):
#    input_lines.append(input())

def count_student_marks(values):
  student_marks = {}

  for value in values:
    (student, mark) = value.split(" ")
    if student not in student_marks:
      student_marks[student]= []
    student_marks[student].append(mark)
  return student_marks

def avg(values):
  return sum(values)/len(values)

def print_result(students_marks):
  for (studen_name, marks) in students_marks.items():
    avg_mark = avg([float(mark) for mark in marks])
    marks_string = ' '.join(f'{float(mark):.2f}' for mark in marks)
    print(f'{studen_name} -> {marks_string} (avg: {avg_mark:.2f})')

test_input = input_to_list(int(input()))

print_result(count_student_marks(test_input))
