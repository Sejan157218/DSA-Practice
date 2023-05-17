def merge_sort(arr):
    length = len(arr)
    if length <=1:
        return
    
    mid = length // 2
    left = arr[:mid]
    right = arr[mid:]
    
    merge_sort(left)
    merge_sort(right)
    return marge_two_sorted_list(left, right, arr)

def marge_two_sorted_list(a, b, arr):
    len_of_a = len(a)
    len_of_b = len(b)
    i=j=k=0
    
    while i < len_of_a and j < len_of_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i +=1
        else:
            arr[k] = b[j]
            j +=1
        k +=1
    while i < len_of_a:
        arr[k] = a[i]
        i +=1
        k +=1
    while j < len_of_b:
        arr[k] = b[j]
        j +=1
        k +=1
    return arr


list1 = [1, 2, 5, 6]

list2 = [3, 4, 7, 8]
list3 = [3, 4, 7, 1, 2, 5, 6, 8]
# print(marge_two_sorted_list(list1, list2))
print(merge_sort(list3))

test_cases = [
    [10, 3, 15, 7, 8, 23, 98, 29],
    [],
    [3],
    [9,8,7,2],
    [1,2,3,4,5]
]

for arr in test_cases:
    merge_sort(arr)
    print(arr)