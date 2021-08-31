"""
    给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
    如果数组中不存在目标值 target，返回 [-1, -1]。
    进阶：
        你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？

    示例1:
        输入：nums = [5,7,7,8,8,10], target = 8
        输出：[3,4]

    示例2:
        输入：nums = [5,7,7,8,8,10], target = 6
        输出：[-1,-1]

    示例3:
        输入：nums = [], target = 0
        输出：[-1,-1]

"""
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
            二分法  分别查找第一个target的下标，以及第一个大于target的下标
        """
        if not nums:
            return [-1,-1]
        def get_first(nums,target):
            left,right = 0,len(nums)-1
            while left<=right:
                mid = (left+right)//2
                if nums[mid]>=target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
        min_ = get_first(nums,target)
        max_ = get_first(nums,target+1) - 1
        if (min_ == len(nums))|(nums[min_]!=target):
            return [-1,-1]
        else:
            return [min_,max_]

print(Solution().searchRange([5,7,7,8,8,10],8))
print(Solution().searchRange([5,7,7,8,8,10],6))
print(Solution().searchRange([],0))