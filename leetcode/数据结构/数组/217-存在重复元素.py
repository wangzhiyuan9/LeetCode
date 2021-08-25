"""
    给定一个整数数组，判断是否存在重复元素。
    如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。

    示例1:
        输入: [1,2,3,1]
        输出: true

    示例2:
        输入: [1,2,3,4]
        输出: false

    示例3:
        输入: [1,1,1,3,3,4,3,2,4,2]
        输出: true
"""


from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        return True


print(Solution().containsDuplicate([1,2,3,1]))
print(Solution().containsDuplicate([1,2,3,4]))
print(Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2]))


# Java解法先对数组排序,之后便历数组，如果数组中的i和i+1位置的值相同，说明存在重复原始返回true
"""
    class Solution {
    public boolean containsDuplicate(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        for(int i=0;i<n-1;i++){
            if(nums[i]==nums[i+1]){
                return true;
            }
        }
        return false;
    }
}
"""
