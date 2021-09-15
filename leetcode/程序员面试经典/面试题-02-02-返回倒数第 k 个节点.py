"""
    实现一种算法，找出单向链表中倒数第 k 个节点。返回该节点的值。
    注意：本题相对原题稍作改动

    示例：
        输入： 1->2->3->4->5 和 k = 2
        输出： 4
"""
from ListNode import ListNode, listnode
class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        fast,slow =  head,head
        for i in range(k):
            fast = fast.next
        while fast:
            fast = fast.next 
            slow = slow.next
        return slow.val
ln = listnode()
l1 = ln.list_node([1, 1, 1, 1, 2])
print(Solution().kthToLast(l1,2))