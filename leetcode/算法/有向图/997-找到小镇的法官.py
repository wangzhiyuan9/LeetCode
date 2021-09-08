"""
    在一个小镇里，按从 1 到 n 为 n 个人进行编号。传言称，这些人中有一个是小镇上的秘密法官。
    如果小镇的法官真的存在，那么：
        小镇的法官不相信任何人。
        每个人（除了小镇法官外）都信任小镇的法官。
        只有一个人同时满足条件 1 和条件 2 。
        给定数组 trust，该数组由信任对 trust[i] = [a, b] 组成，表示编号为 a 的人信任编号为 b 的人。
    如果小镇存在秘密法官并且可以确定他的身份，请返回该法官的编号。否则，返回 -1。

    示例 1：
        输入：n = 2, trust = [[1,2]]
        输出：2
    示例 2：
        输入：n = 3, trust = [[1,3],[2,3]]
        输出：3
"""
from typing import List
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
            有向图  法官的出度为0入度为n-1

        """
        list_ = [0] * n
        for i in trust:
            list_[i[0]-1] -= 1
            list_[i[1]-1] += 1
        for i in list_:
            if i == n-1:
                return i+1
        return -1
print(Solution().findJudge(2,[[1,2]]))