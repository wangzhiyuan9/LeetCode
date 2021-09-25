"""
    编写函数，实现许多图片编辑软件都支持的「颜色填充」功能。
    待填充的图像用二维数组 image 表示，元素为初始颜色值。初始坐标点的行坐标为 sr 列坐标为 sc。需要填充的新颜色为 newColor 。
    「周围区域」是指颜色相同且在上、下、左、右四个方向上存在相连情况的若干元素。
    请用新颜色填充初始坐标点的周围区域，并返回填充后的图像。

    示例：
        输入：
            image = [[1,1,1],[1,1,0],[1,0,1]] 
            sr = 1, sc = 1, newColor = 2
        输出：
            [[2,2,2],[2,2,0],[2,0,1]]
        解释: 
            初始坐标点位于图像的正中间，坐标 (sr,sc)=(1,1) 。
            初始坐标点周围区域上所有符合条件的像素点的颜色都被更改成 2 。
            注意，右下角的像素没有更改为 2 ，因为它不属于初始坐标点的周围区域。
             
    提示：
        image 和 image[0] 的长度均在范围 [1, 50] 内。
        初始坐标点 (sr,sc) 满足 0 <= sr < image.length 和 0 <= sc < image[0].length 。
        image[i][j] 和 newColor 表示的颜色值在范围 [0, 65535] 内。
"""
from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        old_color = image[sr][sc]
        if old_color == newColor:
            return image
        turn_list = [(sr,sc)]
        ind,col =len(image),len(image[0])
        while turn_list:
            x,y = turn_list.pop()
            image[x][y] = newColor
            for i,j in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if 0<=i<ind and 0<=j<col and image[i][j] == old_color:
                    turn_list.insert(0,(i,j))
                    image[i][j] == newColor
        return image

print(Solution().floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))