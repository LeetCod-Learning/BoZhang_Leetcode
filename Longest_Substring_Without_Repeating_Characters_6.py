#3. 无重复字符的最长子串


# 暴力解法 时间复杂度 O（n2）
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         result = [0]
#         for i in range(len(s)):
#             length_list = []
#             if len(s)-i < max(result):
#                 break
#             while True:
#                 if i<=len(s)-1 and s[i] not in length_list:
#                     length_list.append(s[i])
#                     i+=1
#                 else:
#                     break
#             result.append(len(length_list))
#         length = max(result)
#         return length


##
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length_list = [0]
        k = -1  #起始下标
        dict_word = {}
        for num,word in enumerate(s):
            #字符c在字典中 且 上次出现的下标大于当前长度的起始下标
            if word in dict_word and dict_word[word]>k:
                k = dict_word[word]
                dict_word[word] = num
            else:
                dict_word[word] = num
                length_list.append(num - k)

        return max(length_list)




a = Solution()
b="tmmzuxt"

print(a.lengthOfLongestSubstring(b))
