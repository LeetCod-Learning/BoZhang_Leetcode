# Definition for singly-linked list.
#输入：1->2->4, 1->3->4
#输出：1->1->2->3->4->4

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result =ListNode(0)
        node = result

        # 加try是应为要判断发生异常时，一定l1/l2至少一个为None了
        while l1 or l2:
            try:
                a = l1.val
                b = l2.val

                if a<b:
                    node.next = ListNode(a)
                    l1 = l1.next
                    # print('a=',a)
                else:
                    node.next = ListNode(b)
                    l2 = l2.next
                    # print('b=',b)
                node = node.next
            except:
                break

        node.next = l1 or l2    # 接上不为None的节点
        return result.next