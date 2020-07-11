# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        result = ListNode(0)
        node = result
        carry = 0
        sum = 0
        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            sum = (a+b+carry)%10        ##取余数
            carry = (a+b+carry)//10     ##取进位

            node.next = ListNode(sum)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            node = node.next
        if carry != 0:
            node.next = ListNode(carry)
        return result.next


result = ListNode(0)
l1 = result

l1.next = ListNode(2)
l1 = l1.next
l1.next = ListNode(4)
l1 = l1.next
l1.next = ListNode(3)
l1 = l1.next
# l2 = [5,6,4]
# a = Solution()
# a.addTwoNumbers(l1,l2)


print(result.val)
print(result.next.val)
print(result.next.next.val)
print(result.next.next.next.val)

print("*****")
print(l1.val)
print(l1.next.val)
print(l1.next.next.val)
# print(l1.next.next.next.val)

