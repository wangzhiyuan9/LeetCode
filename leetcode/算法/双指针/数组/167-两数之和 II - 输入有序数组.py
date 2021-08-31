"""
    给定一个已按照 升序排列  的整数数组 numbers ，请你从数组中找出两个数满足相加之和等于目标数 target 。
    函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numbers 的下标 从 1 开始计数 ，所以答案数组应当满足 1 <= answer[0] < answer[1] <= numbers.length 。
    你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。

     
    示例 1：
        输入：numbers = [2,7,11,15], target = 9
        输出：[1,2]
        解释：2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。

    示例 2：
        输入：numbers = [2,3,4], target = 6
        输出：[1,3]

    示例 3：
        输入：numbers = [-1,0], target = -1
        输出：[1,2]

"""
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
            双指针
                定义左右指针  左指针为首位   右指针为末位
                左右指针所指值的和 若等于target 返回[left+1,right+1]
                若左右指针所指值的和 小于target 左指针右移一位
                若左右指针所指值的和 大于target 右指针左移一位

                若左右指针的值相等 则说明没有符合条件的数值
        """
        left,right =0,len(numbers)-1
        while left!=right:
            if numbers[left]+numbers[right] == target:
                return [left+1,right+1]
            elif numbers[left]+numbers[right] < target:
                left+=1
            else:
                right -= 1
        return [-1,-1]


print(Solution().twoSum([2,7,11,15],9))
print(Solution().twoSum([2,3,4],6))
print(Solution().twoSum([-1,0],-1))