def insertion_sort_2(n, arr) -> None:
    for i in range(1, n):
        current = arr[i]
        j = i - 1

        while j >= 0:
            if current > arr[j]:
                break

            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = current
        print(arr)

# Test cases
test_cases = [
    (7, [3, 4, 7, 5, 6, 2, 1]),
    (6, [1, 4, 3, 5, 6, 2]),
]

for n, arr in test_cases:
    insertion_sort_2(n=n, arr=arr)