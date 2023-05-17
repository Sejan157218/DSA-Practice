def swap(i, j, arr):
    if i != j:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp


def quick_sort(arr, start, end):
    if start < end:
        pi = partition(arr, start , end)
        print("pi", arr)
        quick_sort(arr, start, pi - 1)
        quick_sort(arr, pi + 1, end)
        
        
def partition(arr, start, end):
    pivot_index = start
    pivot = arr[pivot_index]

    while start < end:
        while start < len(arr) and arr[start] <= pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1
        
        if start < end:
            swap(start, end, arr)
    swap(pivot_index, end, arr)
    
    return end    

    
tests = [
    [11,9,29,7,2,15,28],
    [3, 7, 9, 11],
    [25, 22, 21, 10],
    [29, 15, 28],
    [],
    [6]
]

for elements in tests:
    quick_sort(elements, -1, len(elements)-1)
    print(f'sorted array: {elements}')