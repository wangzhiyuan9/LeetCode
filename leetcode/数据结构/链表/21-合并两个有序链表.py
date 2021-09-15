"""
    将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 


    示例 1：

        输入：l1 = [1,2,4], l2 = [1,3,4]
        输出：[1,1,2,3,4,4]
"""
from ListNode import listnode,ListNode
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dumys = ListNode(0)
        dumy = dumys
        while l1 and l2:
            if l1.val <= l2.val:
                dumy.next = l1
                l1 = l1.next
            else:
                dumy.next = l2
                l2 = l2.next
            dumy = dumy.next
        dumy.next = l1 if l1 is not None else l2 
        return dumys.next

ln = listnode()
l1 = ln.list_node([1,2,4])
l2 = ln.list_node([1,3,4])
print(ln.listNodeToString(Solution().mergeTwoLists(l1,l2)))