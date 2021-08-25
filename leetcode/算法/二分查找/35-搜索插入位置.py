"""
    给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
    如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
    请必须使用时间复杂度为 O(log n) 的算法。

    示例1:
        输入: nums = [1,3,5,6], target = 5
        输出: 2

    示例2:
        输入: nums = [1,3,5,6], target = 2
        输出: 1

    示例3:
        输入: nums = [1,3,5,6], target = 7
        输出: 4

    示例4:
        输入: nums = [1,3,5,6], target = 0
        输出: 0
    
    示例5:
        输入: nums = [1], target = 0
        输出: 0 
"""
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low,height = 0,len(nums)-1
        while low <= height:
            mid = (low+height)//2

            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                height = mid -1
            else:
                low = mid + 1
        return low

print(Solution().searchInsert([1,3,5,6],2))
