"""
    在经典汉诺塔问题中，有 3 根柱子及 N 个不同大小的穿孔圆盘，盘子可以滑入任意一根柱子。
    一开始，所有盘子自上而下按升序依次套在第一根柱子上(即每一个盘子只能放在更大的盘子上面)。移动圆盘时受到以下限制:
        (1) 每次只能移动一个盘子;
        (2) 盘子只能从柱子顶端滑出移到下一根柱子;
        (3) 盘子只能叠在比它大的盘子上。

    请编写程序，用栈将所有盘子从第一根柱子移到最后一根柱子。

    你需要原地修改栈。

    示例1:
        输入：A = [2, 1, 0], B = [], C = []
        输出：C = [2, 1, 0]

    示例2:
        输入：A = [1, 0], B = [], C = []
        输出：C = [1, 0]

    提示:
        A中盘子的数目不大于14个。
"""

from typing import List
class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> List:
        """
        Do not return anything, modify C in-place instead.
        1.当只有一个盘子时，可以直接将其从A移动到C。
        2.当盘子个数大于1时，解决汉诺塔问题，可以分为3步。
            （1）把A上边的n-1盘子通过C移动到B上。
            （2）把A上剩下的一个盘子直接移动到C上。
            （3）把B上的n-1个盘子通过A移动到C上。
        """
        n = len(A)
        self.move(n,A,B,C)
        return C
    def move(self,num,A,B,C):
        if num == 1:
            C.append(A.pop()) 
        else:
            print("0")
            self.move(num-1,A,C,B)
            print("1")
            C.append(A.pop())
            print("2")
            self.move(num-1,B,A,C)
            print("3")


print(Solution().hanota([4,2, 1, 0],[],[]))