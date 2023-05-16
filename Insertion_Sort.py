def Insertion_Sort(arr):
    
    for i in range(1, len(arr)):
        item = arr[i]
        j = i -1

        while j>=0 and arr[j]> item:
            arr[j+1] = arr[j]
            j -=1

        arr[j+1] =item
        
    return arr
            

arr=[-1,5,3,4,0]
# arr=[1,3,2,2,3,1]
print(Insertion_Sort(arr))