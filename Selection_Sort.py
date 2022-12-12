# class Solution:
#     def selectionSort(self, arr):
#         for i in range(len(arr)):
#             min_index=i
#             for j in range(i,len(arr)):
#                 if arr[min_index]>arr[j]:
#                    min_index=j
                  
#             if min_index!=i:
#                 temp=arr[i]
#                 arr[i]=arr[min_index]
#                 arr[min_index]=temp
#         print(arr)
#         pass

# s=Solution()
# arr=[-1,5,3,4,0]

# print(s.selectionSort(arr))



class Solution:
    def selectionSort(self, arr):
        for i in range(len(arr)):
            min_index=i
            for j in range(i,len(arr)):
                if arr[min_index]>arr[j]:
                    min_index=j
            if min_index!=i:
                temp=arr[i]
                arr[i]=arr[min_index]
                arr[min_index]=temp
        return arr


s=Solution()
arr=[-1,5,3,4,0]
arr=[1,3,2,2,3,1]
print(s.selectionSort(arr))