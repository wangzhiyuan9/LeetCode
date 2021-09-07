"""
    给定一个包含了一些 0 和 1 的非空二维数组 grid 。
    一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，
    这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。
    找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。)

    示例 1:
        [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]
        对于上面这个给定矩阵应返回 6。注意答案不应该是 11 ，因为岛屿只能包含水平或垂直的四个方向的 1 。
    示例 2:
        [[0,0,0,0,0,0,0,0]]
        对于上面这个给定的矩阵, 返回 0。
"""
from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
            广度优先算法
            找到岛屿   不断寻找附近的岛屿   以及附近岛屿的岛屿
            并将找到的岛屿转换为0 防止重复
            直到周围都是水

            遍历数组中的每一个值 
            直到找到最大的岛屿
        """

        max_x , max_y = len(grid),len(grid[0])
        def dfs(x,y):
            if (0<=x<max_x) and (0<=y<max_y) and (grid[x][y]==1):
                grid[x][y] = 0
                return 1 + dfs(x-1,y) + dfs(x+1,y) + dfs(x,y-1) + dfs(x,y+1)
            return 0
        res = 0
        for i in range(max_x):
            for j in range(max_y):
                res = max(res,dfs(i,j))
        return res




gd = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(Solution().maxAreaOfIsland(gd))

print(Solution().maxAreaOfIsland([[0,0,0,0,0,0,0,0]]))