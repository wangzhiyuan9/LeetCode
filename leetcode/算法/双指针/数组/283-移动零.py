
"""
    给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

    示例:
        输入: [0,1,0,3,12]
        输出: [1,3,12,0,0]

    说明:
        必须在原数组上操作，不能拷贝额外的数组。
        尽量减少操作次数。

"""
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        第一次遍历:
            count即是游标也是非0元素的个数
            遇到非零元素 
                令count指向的值变为非零元素
                同时令count向右移动移动一位
        第二次遍历
            依据非0元素的个数
            将非零元素以后的值均变为0 
        """
        count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[count] = nums[i]
                count += 1
        for j in range(count,len(nums)):
            nums[j] = 0
        return nums

print(Solution().moveZeroes([0,1,0,3,12]))