from util import time_it
@time_it
def binary_search(list, find_num):
    start = 0
    end = len(list) - 1
    mid_index = 0
    
    while start <= end:
        mid_index = (start + end) //2
        mid_number = list[mid_index]
        
        if mid_number == find_num:
            return mid_index
        
        if mid_number < find_num:
            start = mid_index + 1
        else:
            end = mid_index - 1
    return -1

@time_it
def binary_search_recurcive(list, find_num, left_index, right_index):
    if right_index < left_index:
        return -1
    
    mid_index =( left_index + right_index) //2 
    if mid_index >= len(list) or mid_index < 0:
        return -1
    mid_number = list[mid_index]
    
    if mid_number == find_num:
        return mid_index
    
    if mid_number < find_num:
        left_index = mid_index + 1
        # return binary_search_recurcive(list, find_num, left_index, right_index )
    else:
        right_index = mid_index - 1
        
    return binary_search_recurcive(list, find_num, left_index, right_index )
    
    
    

    


num = [3, 3, 4, 6, 6, 7, 7, 7, 9, 899, 899]
find_num = 633

print("binary_search", binary_search(num, find_num))
print( "binary_search_recurcive", binary_search_recurcive(num, find_num, 0, len(num)))