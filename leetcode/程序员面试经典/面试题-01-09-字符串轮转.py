"""
    字符串轮转。给定两个字符串s1和s2，请编写代码检查s2是否为s1旋转而成（比如，waterbottle是erbottlewat旋转后的字符串）。

    示例1:
        输入：s1 = "waterbottle", s2 = "erbottlewat"
        输出：True
        
    示例2:
        输入：s1 = "aa", s2 = "aba"
        输出：False
"""
class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        """把S2的尾巴连上S2的头,中间是S1"""
        if len(s1) != len(s2):
            return False
        if s1 in s2+s2:
            return True
        return False

print(Solution().isFlipedString('aba','bab'))
print(Solution().isFlipedString('aba','aab'))


