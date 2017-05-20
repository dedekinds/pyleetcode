'''349_Intersection of Two Arrays
   2017.5.20
   42ms
   beats 88.98%
'''

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1)&set(nums2))

集合操作http://blog.csdn.net/business122/article/details/7541486
可以将set转换为list来处理，真好