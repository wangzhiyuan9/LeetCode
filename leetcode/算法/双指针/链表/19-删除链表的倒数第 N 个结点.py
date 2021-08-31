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
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def list_node(numbers):
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next
    ptr = dummyRoot.next
    return ptr
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pass
    
print(Solution().removeNthFromEnd(list_node([1,2,3,4,5]),2))