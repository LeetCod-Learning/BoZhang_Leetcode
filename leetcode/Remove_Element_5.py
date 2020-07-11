# class Solution:
#     def removeElement(self, nums, val):
#         while True:
#             if val in nums:
#                 nums.remove(val)
#             else:
#                 break
#         return len(nums)
#

class Solution:
    def removeElement(self, nums, val) -> int:
        for i in range(len(nums)-1, -1, -1):
            if(nums[i] == val):
                nums.pop(i)
        print(len(nums))
        print(nums)
        return len(nums)





a = Solution()
nums = [0,1,2,2,3,0,4,2]
val = 2
a.removeElement(nums,val)
