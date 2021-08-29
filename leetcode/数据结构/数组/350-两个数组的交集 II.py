"""
    给定两个数组，编写一个函数来计算它们的交集
    示例1:
        输入：nums1 = [1,2,2,1], nums2 = [2,2]
        输出：[2,2]

    示例2:
        输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
        输出：[4,9]

    说明：
        输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
        我们可以不考虑输出结果的顺序。
    进阶：
        如果给定的数组已经排好序呢？你将如何优化你的算法？
        如果 nums1 的大小比 nums2 小很多，哪种方法更优？
        如果 nums2 的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
"""
from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
            哈希表
        """
        dict_,res={},[]
        # 将nums1中的元素作为键，出现的次数作为值存放到字典中
        for i in nums1:
            if i in dict_:
                dict_[i] += 1
            else:
                dict_[i] = 1
        # 遍历nums2如果nums2中的值在字典中  
        # 并且对应的值大于等于1则存入结果表，且将字典对应值减一
        for i in nums2:
            if i in dict_ and dict_[i]>0:
                res.append(i)
                dict_[i] -= 1
        return res

print(Solution().intersect([1,2,2,1],[2,2]))
print(Solution().intersect([4,9,5], [9,4,9,8,4]))



class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
            双指针
                1.将列表进行排序
                2.定义两个指针分别指向两个数组的首位
                3.比较两个指针所指的数
                    (1)如果相等 则将对应的数值存入res表并将两个指针都右移一位
                    (2)若不相等 则数值小的指针右移一位
                4.任意一个列表遍历结束则表示另一方的剩余值都是独一值
        """
        def sorted_(nums):
            for j in range(len(nums)):
                for i in range(len(nums)-j-1):
                        if nums[i]>nums[i+1]:
                            nums[i],nums[i+1]=nums[i+1],nums[i]
            return nums
        nums1,nums2 = sorted_(nums1),sorted_(nums2)
        i,j=0,0
        res = []
        while ((i<len(nums1))&(j<len(nums2))):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1 
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return res
print(Solution().intersect([1,2,2,1],[2,2]))
print(Solution().intersect([4,9,5], [9,4,9,8,4]))