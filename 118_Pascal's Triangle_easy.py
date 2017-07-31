'''118. Pascal's Triangle 
   2017.7.31
'''

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans=[]
        n=0
        if numRows==0:return ans
        Y=[1]
        while n<numRows:
            ans.append(Y)
            Y=[1]+[Y[i-1]+Y[i] for i in range(len(Y)) if i>0]+[1]
            n+=1
        return ans
        