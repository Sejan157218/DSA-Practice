class Solution:
    def Bubble_Sort(self, arr):

        for i in range(len(arr)):
            for j in range(len(arr)-i-1):
                if arr[j]>arr[j+1]:
                    temp=arr[j+1]
                    arr[j+1]=arr[j]
                    arr[j]=temp
        return arr


s=Solution()
arr=[-1,5,3,4,0]
# arr=[1,3,2,2,3,1]
print(s.Bubble_Sort(arr))