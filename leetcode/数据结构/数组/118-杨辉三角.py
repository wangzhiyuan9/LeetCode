"""
    给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
    在「杨辉三角」中，每个数是它左上方和右上方的数的和。
      1
    1   1
   1  2  1   i=3  j=1
 1  3   3  1

    示例 1:
        输入: numRows = 5
        输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

    示例 2:
        输入: numRows = 1
        输出: [[1]]
"""

from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        list_ = []
        for i in range(1,numRows+1):
            list_append = list_.append
            if i == 1:
                list_append([1])
            else:
                lis_ = []
                lis_append = lis_.append
                for j in range(i):
                    if (j == 0)|(j==i-1):
                        lis_append(1)
                    else:
                        x = list_[i-2][j] + list_[i-2][j-1] 
                        lis_append(x)
                list_append(lis_)
        return list_

print(Solution().generate(4))



