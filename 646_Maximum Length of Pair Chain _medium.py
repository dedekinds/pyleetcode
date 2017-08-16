'''646. Maximum Length of Pair Chain 
   2017.8.16
'''

class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key=lambda x:x[1])
        temp=pairs[0]
        ans=1
        for x in pairs:
            if x[0]>temp[1]:
                ans+=1
                temp=x
        return ans