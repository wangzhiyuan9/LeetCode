"""
    给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，
    使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。
    你不需要 保留 每个分区中各节点的初始相对位置。

    示例 1：
        输入：head = [1,4,3,2,5,2], x = 3
        输出：[1,2,2,4,3,5]

    示例 2：
        输入：head = [2,1], x = 2
        输出：[1,2]
"""
from ListNode import ListNode, listnode
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # 定义两个指针
        left = left_dumy = ListNode(0)
        right = right_dumy = ListNode(0)
        while head:
            if head.val<x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = head.next
        right.next = None
        left.next = right_dumy.next
        return left_dumy.next

ln = listnode()
l1 = ln.list_node([1,4,3,2,5,2])
print(ln.listNodeToString(Solution().partition(l1,3)))