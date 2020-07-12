#注意两种情况
#1，空集，有步长
#2，在一次duration中可能会有多次重复

class Solution:
    def findPoisonedDuration(self, timeSeries, duration) -> int:
        step = 0
        for i in range(len(timeSeries) - 1):
            if timeSeries[i+1] - timeSeries[i]<duration:
                step += timeSeries[i+1] - timeSeries[i]
            else:
                step += duration
        if len(timeSeries) != 0:
            step += duration
        return step

# a = Solution()
# b =[]
# c = 2
# print(a.findPoisonedDuration(b,c))