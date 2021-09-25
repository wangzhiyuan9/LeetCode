"""
    设计一个算法，算出 n 阶乘有多少个尾随零。

    示例 1:
        输入: 3
        输出: 0
        解释: 3! = 6, 尾数中没有零。

    示例 2:
        输入: 5
        输出: 1
        解释: 5! = 120, 尾数中有 1 个零.
        说明: 你算法的时间复杂度应为 O(log n) 。
"""

class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
            计算阶乘中 2*5 的个数
            2的个数肯定比5多   因此5的个数 就是 2*5的个数
        """
        if n == 0: return 0
        s = 0
        while n > 0:
            n = n // 5
            s += n
        return s
print(Solution().trailingZeroes(3))