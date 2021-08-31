"""
    给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
    进阶：你能尝试使用一趟扫描实现吗？
 
    示例 1：

    输入：head = [1,2,3,4,5], n = 2
    输出：[1,2,3,5]

    示例 2：
    输入：head = [1], n = 1
    输出：[]

    示例 3：
    输入：head = [1,2], n = 1
    输出：[1]

"""

from ListNode import listnode,ListNode
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
            快慢双指针
            快的指针比慢的指针快n  因此快指针到达尾部时 慢指针正好指向倒数第n个节点
        """
        fast = head
        dummy = ListNode(0,head)
        slow = dummy
        for i in range(n):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next



        """
            计算链表长度

        pre = head
        count = 0
        while pre:
            count += 1
            pre = pre.next        
        dummy = ListNode(0, head)
        cur = dummy
        for i in range(1,count-n+1):
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next
        """

ln = listnode()
res = Solution().removeNthFromEnd(ln.list_node([1,2,3,4,5]),2)
print(ln.listNodeToString(res))
