import re

pattern = r"(@#{1,})([A-Z]{1}[0-9A-Za-z]{4,}[A-Z]{1,})(@#{1,})"

count_of_barcodes = int(input())
barcode=''
for i in range(count_of_barcodes):
  barcode = input()
  match = re.fullmatch(pattern,barcode)

  if match is None:
    print(f"Invalid barcode")
    continue
  
  product=match[2]
  group = ''
  for j in range(len(product)):
    if product[j].isdigit():
      group+=product[j]


  if group=='':
    group = '00'
    print(f'Product group: {group}')
  else:
    print(f'Product group: {group}')

  
