class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class listnode:
    def list_node(self,numbers):
        dummyRoot = ListNode(0)
        ptr = dummyRoot
        for number in numbers:
            ptr.next = ListNode(number)
            ptr = ptr.next
        ptr = dummyRoot.next
        return ptr
    def listNodeToString(self,node):
        if not node:
            return "[]"

        result = ""
        while node:
            result += str(node.val) + ", "
            node = node.next
        return "[" + result[:-2] + "]"