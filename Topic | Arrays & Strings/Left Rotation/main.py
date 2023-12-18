def index_helper(index, length) -> int:
    if index >= length:
        return index - length
    else:
        return index

def rot_left(a, d) -> list[int]:
    a1 = []
    rotation = d % len(a)

    if rotation == 0:
        return a
    
    for i in range(len(a)):
        index = index_helper(index=i + rotation, length=len(a))
        a1.append(a[index])
    
    return a1

a = [1, 2, 3, 4, 5]
d = 4
result = rot_left(a=a, d=d)
print(result)

a = [1, 2, 3, 4, 5]
d = 2
result = rot_left(a=a, d=d)
print(result)