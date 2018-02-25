'''
788. Rotated Digits
2018.2.25
'''

class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        ans=0
        for x in range(1,N+1):
            temp=str(x)
            if '3' in temp or '4' in temp or '7'in temp:
                continue
            if '2' in temp or '5' in temp or '6' in temp or '9' in temp:
                ans+=1
        return ans