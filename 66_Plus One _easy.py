'''599. Minimum Index Sum of Two Lists
   2017.6.4
   45ms
   beats 58.83%
'''

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        A=digits[::-1]
        #反转、满9进位，最后也进位的话再append一个1，最后再反转
        for x in range(len(A)):
            temp=A[x]+1
            if temp==10:
                A[x]=0
            else:
                A[x]=A[x]+1
                break
        if A[-1]==0:
            A.append(1)      
        return A[::-1] 