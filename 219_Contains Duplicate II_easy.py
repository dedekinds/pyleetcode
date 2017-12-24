'''
219. Contains Duplicate II
2017.12.24
'''
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        temp=dict()
        for x in range(len(nums)):
            
            if temp.get(nums[x],-1)==-1:
                temp[nums[x]]=x
            else:
                if abs(temp[nums[x]]-x)<=k:
                    return True
                else:
                    temp[nums[x]]=x
        return False