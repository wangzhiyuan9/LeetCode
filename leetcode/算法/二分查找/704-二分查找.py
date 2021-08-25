"""
    给定一个 n 个元素有序的（升序）整型数组 nums 
    和一个目标值 target  ，
    写一个函数搜索 nums 中的 target，
    如果目标值存在返回下标，否则返回 -1。

    示例1:
        输入: nums = [-1,0,3,5,9,12], target = 9
        输出: 4
        解释: 9 出现在 nums 中并且下标为 4

    示例2:  
        输入: nums = [-1,0,3,5,9,12], target = 2
        输出: -1  
        解释: 2 不存在 nums 中因此返回 -1
"""
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        height = len(nums) - 1 # 获取列表最大的下标
        while low<=height:
            mid = (low+height) // 2 # 获取中间下标   //为取整
            if nums[mid] == target: # 当查中间值为目标值时返回下标
                return mid
            elif nums[mid] > target: # 当中间值大于目标值,说明目标值在中间值的左面
                height = mid -1      # 将中间值的下标左移一位赋值给height
            elif nums[mid]<target: # 当中间值小于目标值,说明目标值在中间值的右面
                low = mid + 1     # 将中间值的下标右移一位赋值给low
        return -1 # 未查询到时返回-1
print(Solution().search([-1,0,3,5,9,12],9))
print(Solution().search([-1,0,3,5,9,12],2))


"""
    #java解法
    class Solution {
    public int search(int[] nums, int target) {
        int low = 0;
        int height = nums.length-1;
        int mid;
        while(low<=height){
            mid = low+(height-low)/2; //相当于(height+low)/2,可以防止溢出
            if(nums[mid]==target){
                return mid;
            }if(nums[mid]>target){
                height=mid-1;
            }else{
                low=mid+1;
            }
        }
        return -1;
    }
    } 
"""
