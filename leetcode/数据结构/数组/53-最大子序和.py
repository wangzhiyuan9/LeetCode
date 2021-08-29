"""
    给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
    示例1:
        输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
        输出：6
        解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

    示例2:
        输入：nums = [1]
        输出：1

    示例3:
        输入：nums = [0]
        输出：0

    示例4:
        输入：nums = [-1]
        输出：-1

    示例5:
        输入：nums = [-100000]
        输出：-100000
"""
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
            '''
                贪心算法
            '''
            max_num = nums[0]
            pre = 0
            for i in nums:
                pre = max(pre+i,i)
                max_num = max(pre,max_num)
            return max_num

print(Solution().maxSubArray([1]))
print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))