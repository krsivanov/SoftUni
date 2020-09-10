start_number = int(input())
end_number = int(input())

# print(
#     [x for x in range(start_number, end_number + 1)
#      if len(
#         [True for d in range(2, 11) if x % d == 0]
#     )>0
#      ]
# )

print(
    [x for x in range(start_number,end_number+1)
     if any([x%d == 0 for d in range(2,11)])
    ]
)

