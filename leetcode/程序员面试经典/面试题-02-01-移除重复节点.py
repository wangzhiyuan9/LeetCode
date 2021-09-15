"""
    编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。

    示例1:
        输入：[1, 2, 3, 3, 2, 1]
        输出：[1, 2, 3]

    示例2:
        输入：[1, 1, 1, 1, 2]
        输出：[1, 2]
"""
from ListNode import ListNode, listnode

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        hash_ = {}
        dumy = ListNode(0,head)
        p = dumy
        while p.next:
            cur = p.next
            if cur.val in hash_:
                p.next = p.next.next
            else:
                hash_[cur.val] = 1
                p = p.next
        return dumy.next 

ln = listnode()
l1 = ln.list_node([1, 1, 1, 1, 2])
print(ln.listNodeToString(Solution().removeDuplicateNodes(l1)))