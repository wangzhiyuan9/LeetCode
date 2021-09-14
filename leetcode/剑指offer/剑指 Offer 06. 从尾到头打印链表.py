"""
    输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
    示例 1：

        输入：head = [1,3,2]
        输出：[2,3,1]
"""
from ListNode import listnode,ListNode
from typing import List
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        s = []
        while head:
            s.insert(0,head.val) 
            head = head.next
        return s
ln = listnode()
res = ln.list_node([1,2,4,5])
print(Solution().reversePrint(res))