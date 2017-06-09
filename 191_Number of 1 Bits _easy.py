'''191. Number of 1 Bits  
   2017.6.9

'''
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=0
        while n:
            if n&1==1:
                ans+=1
            n=n>>1
        return ans
        
'''
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(0^n).count('1')    
'''

'''
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n > 0:
            res += 1
            n = n & (n - 1)
        return res

'''