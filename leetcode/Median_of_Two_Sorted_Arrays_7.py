### 错误思路！！！！


class Solution:
    def findMedianSortedArrays(self, list1, list2):
        if len(list1) == 0:
            if len(list2)%2 == 0:
                return ( list2[int(len(list2)/2)] + list2[int(len(list2)/2 - 1)] ) /2
            else:
                return list2[int( (len(list2)-1 /2))]

        if len(list2) == 0:
            if len(list1)%2 == 0:
                return ( list1[int(len(list1)/2)] + list1[int(len(list1)/2 - 1)] ) /2
            else:
                return list1[int( (len(list1)-1 /2))]

        return self.find_median(list1,list2)


    def find_median(self,list1, list2):
        ### 条件
        if len(list1) > len(list2):
            return self.find_median(list2,list1)
        if len(list1) == 1 and len(list2) == 1:
            return (list1[0] + list2[0])/2


        length1 = len(list1)
        length2 = len(list2)
        ### 判断奇偶数，找每个列表中位数
        if length1 % 2 == 1:
            mid_1 = list1[int(((length1 - 1) / 2))]
        if length1 % 2 == 0:
            mid_1 = ( list1[int(length1/2)] + list1[int(length1 /2 - 1)] ) / 2

        if length2 % 2 == 1:
            mid_2 = list2[int(((length2 - 1) / 2))]
            t =  int((length2 - 1) / 2)
        if length2 % 2 == 0:
            mid_2 = ( list2[int(length2/2)] + list2[int(length2/2 - 1)] ) / 2
            t = int(length2/2)

        if mid_1 > mid_2:
            return self.find_median(list1,list2[t:])
        if mid_1 < mid_2:
            return self.find_median(list1,list2[:t])
        if mid_1 == mid_2:
            return mid_1


a= Solution()
x=[3]
y=[-2,-1]
o = a.findMedianSortedArrays(x,y)
print(o)
