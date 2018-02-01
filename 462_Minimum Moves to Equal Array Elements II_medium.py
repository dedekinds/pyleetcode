'''
462. Minimum Moves to Equal Array Elements II
2018.2.2
'''
import collections
class Solution:
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #O(n)
        #http://blog.csdn.net/li4951/article/details/7486092
        #小飞电梯调度问题
        #如果是非负数的话就有下面的代码
        person=collections.Counter(nums)
        N1=0
        N2=person[0]
        N3=0
        ans=0
        #计算N3
        for x in range(1,max(nums)+1):
            N3+=person[x]
            ans+=person[x]*(x)
        
        for x in range(1,max(nums)+1):
            if N1+N2-N3<0:
                ans+=(N1+N2-N3)
                N3-=person[x]
                N1+=N2
                N2=person[x]
            else:
                break
        return ans
                
                
        
        
        
        ____________________________________________
        #O(nlogn)
        nums.sort()
        medium=nums[len(nums)>>1]
        return sum( abs(x-medium) for x in nums)
                
        
