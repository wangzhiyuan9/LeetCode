"""
    定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

    示例:
        输入: 1->2->3->4->5->NULL
        输出: 5->4->3->2->1->NULL
"""
from ListNode import listnode,ListNode
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        s = ListNode().next
        while head:
            s = ListNode(head.val,s)
            head = head.next
        return s
ln = listnode()
res = ln.list_node([1,2,4,5])
print(ln.listNodeToString(Solution().reverseList(res)))