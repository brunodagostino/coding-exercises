def a_very_big_sum(ar) -> int:
    sum = 0
    i = 0

    while i < len(ar):
        sum += ar[i]
        i += 1
    
    return sum

ar = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]

sum = a_very_big_sum(ar=ar)
print(sum)