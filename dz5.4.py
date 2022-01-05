src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


result = [
    a for a in src
    if src.count(a) == 1
]
print(result)

# for i in range(len(src)):
#     for j in range(len(src)):
#         if src[i] == src[j] and i != j:
#             break
#             # result.append(src)
#         else:
#             print(src[i])

#         result.append(i)
# print(result)


list_1 = set()
list_2 = set()
for i in src:
    if i not in list_2:
        list_1.add(i)
    else:
        list_1.discard(i)
    list_2.add(i)
print(list_1)
print(list_2)

list_1_src = [i for i in src if i in list_1]
print(list_1_src)