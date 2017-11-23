'''
350. Intersection of Two Arrays II 
2017.11.23
'''
用hash表来记录元的数量，暴力，实际上也就是O(max(m,n))
import collections
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1)>len(nums2):#处理短的那个数组
            nums1,nums2=nums2,nums1
        temp=collections.Counter(nums1)#key的出现顺序是根据计数的从大到小
        ans=[]
        for x in nums2:
            if temp[x]>0:
                ans.append(x)
                temp[x]-=1
        return ans