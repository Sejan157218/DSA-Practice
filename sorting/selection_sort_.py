def selection_sort(arr):
    size = len(arr)
    
    for i in range(size - 1):
        min_index = i
        for j in range(min_index + 1,size):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        


tests = [
    [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
    [],
    [1,5,8,9],
    [234,3,1,56,34,12,9,12,1300],
    [5]
]
elements = [89,78,61,53,23,21,17,12,9,7,6,2,1]
selection_sort(elements)
print(elements)
for elements in tests:
    selection_sort(elements)
    print(elements)