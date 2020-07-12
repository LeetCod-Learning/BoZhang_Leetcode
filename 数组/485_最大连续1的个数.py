# 输入: [1,1,0,1,1,1]
# 输出: 3
# 解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
#
# 输入的数组只包含 0 和1。
# 输入数组的长度是正整数，且不超过 10,000。\


#思路一，双循环遍历，每个元素检查后面连续的数字，时间复杂度较高，最坏达到 O（n2）
#思路二，用enumerate遍历一次，修改index，时间复杂度，O（n）

class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        first_element = nums[0]
        index = 0
        max_length = 1
        for i,j in enumerate(nums):
            if i == 0:
                pass

            if j == first_element:
                max_length = max(max_length,i-index+1)
            else:
                first_element = j
                index = i

        return max_length

a = Solution()
b =[1,1,0,1,1,1,1,0,0,0,0,0,1,0,1,0]
print(a.findMaxConsecutiveOnes(b))