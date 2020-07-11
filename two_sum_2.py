# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

###1.暴力解法 时间复杂度O（n2）空间复杂度O（1）
# class Solution:
#     def twoSum(self, nums, target) :
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i]+nums[j] == target:
#                     result = [i,j]
#         return result

###2.排序+双指针
# class Solution:
#     def twoSum(self, nums, target) :
#         copy_list = nums.copy()
#         copy_list.sort()
#         print(copy_list)
#         i=0
#         j=len(nums)-1
#         while True:
#             if copy_list[i]+copy_list[j]<target:
#                 i+=1
#             elif copy_list[i]+copy_list[j]>target:
#                 j-=1
#             else:
#                 break
#         a = nums.index(copy_list[i])
#         nums.pop(a)
#         b = nums.index(copy_list[j])
#         if b>=a:
#             b+=1
#         result = [a,b]
#         return result


##hash法，遍历nums[i]时，看target-nums[i]是否存在hash表中即可
class Solution:
    def twoSum(self, nums, target):
        hash_dict={}
        for i in range(len(nums)):
            if hash_dict.get(target-nums[i]) is not None:
                return [hash_dict[target-nums[i]],i]
            hash_dict[nums[i]]=i





# nums = [2, 7, 11, 15]
nums = [-1,-2,-3,-4,-5]

target = -8
a=Solution()
print(a.twoSum(nums,target))

# a = {'one':1,'two':2}
# print(a.get('one'))
# print(a.get('sad'))
# print(a['dw'])