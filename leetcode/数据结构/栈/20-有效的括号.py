"""
    给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
    有效字符串需满足：
    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。
     

    示例 1：
        输入：s = "()"
        输出：true
        
    示例 2：
        输入：s = "()[]{}"
        输出：true
        
    示例 3：
        输入：s = "(]"
        输出：false
        
    示例 4：
        输入：s = "([)]"
        输出：false
        
    示例 5：
        输入：s = "{[]}"
        输出：true
"""
class Solution:
    def isValid(self, s: str) -> bool:
        """
            先判断字符串长度是否为奇数
            
            栈 后进先出
            如果为反括号判断栈顶元素是否为相应的括号
                True:栈顶元素出栈
                False:说明括号不合法
            若为正括号则将元素入栈
        """
        if len(s) % 2 == 1:
            return False
        dicts = {')':'(','}':'{',']':'['}
        stack = []
        for i in s:
            if i not in dicts:
                stack.append(i)
            else:
                if not stack or stack[-1]!=dicts[i]:
                        return False
                stack.pop()
        return not stack
print(Solution().isValid("{[]}"))
print(Solution().isValid("([)]"))
print(Solution().isValid("(]"))
print(Solution().isValid("()[]{}"))
print(Solution().isValid("}"))
print(Solution().isValid("{{"))
