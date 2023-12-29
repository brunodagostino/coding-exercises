def partition(arr, low, high) -> int:
    pivot = arr[low]

    i = (low + 1)
    for j in range(low + 1, high + 1):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[low], arr[i - 1] = arr[i - 1], arr[low]

    print(arr)

    return (i - 1)

def quick_sort(arr, low, high) -> None:
    if low < high:
        pi = partition(arr=arr, low=low, high=high)
        quick_sort(arr=arr, low=low, high=pi - 1)
        quick_sort(arr=arr, low=pi + 1, high=high)


# Test cases
test_cases = [
    (7, [5, 8, 1, 3, 7, 9, 2])
]

for n, ar in test_cases:
    quick_sort(arr=ar, low=0, high=n - 1)