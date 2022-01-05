src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [
    a for i, a in zip(src, src[1:]) if a > i
]
print(result)



