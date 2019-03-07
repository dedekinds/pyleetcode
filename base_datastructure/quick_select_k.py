
import random
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        temp = random.choice(nums)
        nums1 = []
        nums2 = []
        for val in nums:
            if val > temp:nums1.append(val)
            if val < temp:nums2.append(val)
        if k <= len(nums1):
            return self.findKthLargest(nums1,k)
        if k > len(nums)-len(nums2):
            return self.findKthLargest(nums2,k - (len(nums)-len(nums2)))
        return temp
        