class Solution:
    def Insertion_Sort(self, nums):

        for i in range(1,len(nums)):
            item=nums[i]
            j=i-1
            while j>=0 and nums[j]>item:
                nums[j+1]=nums[j]
                j-=1
            nums[j+1]=item
     
        return nums
s=Solution()
arr=[-1,5,3,4,0]
# arr=[1,3,2,2,3,1]
print(s.Insertion_Sort(arr))