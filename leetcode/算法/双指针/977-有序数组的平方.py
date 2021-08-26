"""
    给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
    示例1:
        输入：nums = [-4,-1,0,3,10]
        输出：[0,1,9,16,100]
        解释：平方后，数组变为 [16,1,0,9,100]
        排序后，数组变为 [0,1,9,16,100]
    示例2:
        输入：nums = [-7,-3,2,3,11]
        输出：[4,9,9,49,121]
"""
from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
            双指针
            1.先新建一个全0的数组用于存储结果
            2.创建左右指针和游标(左指针初始为0, 右指针和游标初始为数组最后一个元素的下标)
            3.比较左指针与右指针所指元素平方的大于，将较大的值放在结果数组中游标所指位置
            4.若左指针的元素平方较大,将左指针右移动
            5.游标左移
            6.重复3-5步，直到左指针大于右指针
        """
        len_ = len(nums)
        # 定义指针
        left,right=0,len_-1
        # 定义游标
        cur = len_-1
        # 定义新数组用于存储结果
        res = [0]*len_
        while right>=left:
            right_= pow(nums[right],2)
            left_ = pow(nums[left],2)
            if  right_>left_ :
                res[cur]=right_
                right -= 1
            else:
                res[cur]=left_
                left+=1
            cur-=1
        return res

print(Solution().sortedSquares([-4,-1,0,3,10]))
print(Solution().sortedSquares([-7,-3,2,3,11]))