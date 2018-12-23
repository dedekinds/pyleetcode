class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        temp = {}
        for i in A:
            if i not in temp.keys():
                temp[i] = 1
            else:
                return i


If a number is repeated N times in a list of size 2N, it is always possible for the repeated number to stay within a distance of 2.
Consider this exaple where N = 4, Number x is repeated twice. All possible comibnations for x to fit in a list of size 4 are:
[a,b,x,x]
[x,a,b,x] (distance between both the x is still 1, consider it as a circular list)
[x,a,x,b]
[x,x,a,b]
[a,x,b,x]
[a,x,x,b]
神奇的做法
class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for temp in range(len(A)):
            if A[temp - 1] == A[temp] or A[temp - 2] == A[temp]:
                return A[temp]