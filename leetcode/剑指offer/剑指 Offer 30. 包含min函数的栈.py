"""
    定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，
    调用 min、push 及 pop 的时间复杂度都是 O(1)。

    示例:

        MinStack minStack = new MinStack();
        minStack.push(-2);
        minStack.push(0);
        minStack.push(-3);
        minStack.min();   --> 返回 -3.
        minStack.pop();
        minStack.top();      --> 返回 0.
        minStack.min();   --> 返回 -2.
"""
class MinStack:
    """
        构建最小值辅助栈 辅助栈的栈顶元素存放存储栈的最小值
        新增元素时 
            对辅助栈的栈顶元素和新增元素比较 
            辅助栈为空或辅助栈的栈顶元素大于等于新增元素时 
            辅助栈也要进行push操作
        移除元素时 
            若辅助栈的栈顶元素与移除值相等
            辅助栈的栈顶元素也要移除
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        # 存储栈
        self.A=[]
        # 栈顶放置最小值
        self.B=[]

    def push(self, x: int) -> None:
        self.A.append(x)
        if not self.B or self.B[-1] >= x:
            self.B.append(x)
    def pop(self) -> None:
        if self.A.pop() == self.B[-1]:
            self.B.pop()

    def top(self) -> int:
        return self.A[-1]

    def min(self) -> int:
        return self.B[-1]

obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
param_1 = obj.min()
obj.pop()
param_2 = obj.top()
param_3 = obj.min()
print(param_1,param_2,param_3)