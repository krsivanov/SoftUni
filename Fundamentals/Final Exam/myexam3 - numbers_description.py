integers = list(map(int, input().split()))
top_5 = []
average = sum(integers) / len(integers)

for i in integers:
    if i > average:
        top_5.append(i)


top_5.sort(reverse= True)

if len(top_5)>=5:
    for i in range(5):
        print(top_5[i], end=' ')
elif len(top_5)==0:
    print('No')
else:
    for i in range(len(top_5)):
        print(top_5[i], end=' ')