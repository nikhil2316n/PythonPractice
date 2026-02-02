# lst = [12, 1, 1, 12, 3, 68, 25, 31]
# i = 0
# while i < len(lst):
#     j = i + 1
#     while j < len(lst):
#         if lst[i] == lst[j]:
#             lst.pop(j)
#         else:
#             j += 1
#     i += 1
# print(lst)


lst = [12, 1, 1, 12, 3, 68, 25, 31]

uniq=[]
for x in lst:
    if x not in uniq:
        uniq.append(x)

print(uniq)