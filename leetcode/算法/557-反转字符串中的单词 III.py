"""
    给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

    示例：
        输入："Let's take LeetCode contest"
        输出："s'teL ekat edoCteeL tsetnoc"

"""

from typing import List
class Solution:
    def reverseWords(self, s: str) -> str:
        res = ''
        for i in s.split(' '):
            res = res + self.reverse(i) + ' '
        return res[:-1]

    def reverse(self,s):
        head = s[-1]
        len_ = len(s)-1
        for i in range(1,len_+ 1):
            head += s[len_-i]
        return head

print(Solution().reverseWords("Let's take LeetCode contest"))


