def bubble_sort(list):
    
    leng_of_list = len(list) - 1
    for i in range(leng_of_list):
        for j in range(leng_of_list - i):
            if list[j] > list[j+1]:
                temp = list[j + 1]
                list[j+1] = list[j]
                list[j] = temp

    return list



arr=[-1,5,3,4,0]
arr=[1,3,2,2,3,1]
print(bubble_sort(arr))