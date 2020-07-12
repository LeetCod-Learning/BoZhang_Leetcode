# 输入: [1,1,0,1,1,1]
# 输出: 3
# 解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
# 输入的数组只包含 0 和1。
# 输入数组的长度是正整数，且不超过 10,000。\

#思路一，使用count统计1的个数，遇见0重新计数
#思路二，将数组划分为字符串，统计字符串个数,一行代码
# return max(map(len, ''.join(map(str, nums)).split('0')))


class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        if len(nums) == 0:
            return 0
        count = 0
        max_length = 0
        for i in nums:
            if i:
                count +=1
                max_length = max(max_length,count)
            else:
                count = 0
        return max_length
#
# a = Solution()
# b =[1,1,0,1,1,1,1,0,0,0,0,0,1,0,1,0]
# c = max(map(len, ''.join(map(str, b)).split('0')))
