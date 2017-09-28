'''215. Kth Largest Element in an Array 
   2017.9.4
'''
使用快速选择，算法导论P120，O(n)
首先选择一个随机数，将数组分成两部分，较大的一部分叫nums1,较小的一部分叫nums2
1.如果k<=len(nums1)，那么其余部分丢掉，直接找nums1中最大的k数就可以了(?)
2.如果不是的话，那么k>len(nums1)
  1.若k<=len(nums)-len(nums2)，结合k>len(nums1)，就知道随机数恰好就是第k大的数
  2.若k>len(nums)-len(nums2)，因为已经有len(nums1)个较大的数，所以返回
  findKthLargest(nums2, k - (len(nums) - len(nums2)))即可

  
import random
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        pivot = random.choice(nums)
        nums1, nums2 = [], []
        for num in nums:
            if num > pivot:
                nums1.append(num)
            elif num < pivot:
                nums2.append(num)
        if k <= len(nums1):
            return self.findKthLargest(nums1, k)
        if k > len(nums) - len(nums2):
            return self.findKthLargest(nums2, k - (len(nums) - len(nums2)))
        return pivot
        
        """
        return sorted(nums)[len(nums)-k]       
        """
