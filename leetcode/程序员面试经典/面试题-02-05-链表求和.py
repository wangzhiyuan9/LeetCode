"""
    给定两个用链表表示的整数，每个节点包含一个数位。
    这些数位是反向存放的，也就是个位排在链表首部。
    编写函数对这两个整数求和，并用链表形式返回结果。
     

    示例：
        输入：(7 -> 1 -> 6) + (5 -> 9 -> 2)，即617 + 295
        输出：2 -> 1 -> 9，即912
        进阶：思考一下，假设这些数位是正向存放的，又该如何解决呢?
    
    示例：
        输入：(6 -> 1 -> 7) + (2 -> 9 -> 5)，即617 + 295
        输出：9 -> 1 -> 2，即912
"""

from ListNode import ListNode, listnode
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        i = 0
        p = dumy = ListNode(0)
        tmp = 0
        while l1 or l2:
            if l1 is None:
                res = l2.val
                l2 = l2.next
            elif l2 is None:
                res = l1.val 
                l1 = l1.next
            else:
                 res = l2.val+l1.val
                 l2 = l2.next
                 l1 = l1.next
            res += tmp
            if res > 9:
                tmp = 1
                res %= 10
            else:
                tmp = 0
            i += 1
            p.next =ListNode(res)
            p = p.next
        if tmp == 1:
            p.next = ListNode(1)
        return dumy.next
ln = listnode()
l1 = ln.list_node([7,1,6])
l2 = ln.list_node([5,9,2])
print(ln.listNodeToString(Solution().addTwoNumbers(l1,l2)))