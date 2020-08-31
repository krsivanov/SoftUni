def count_numbers(values):
  values_count = {}

  for value in values:
    if value not in values_count:
      values_count[value] = 0
    values_count[value] += 1
  return values_count

def print_result(values_counts):
  for (value, count) in values_counts.items():
    print(f'{value} - {count} times')

print_result(
  count_numbers(
    map(
      float, input().split(' ' ))))
