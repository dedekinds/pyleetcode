(i,j) -> (j,k) 找到这样的合法链表
import collections
class Solution(object):
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        index = {x: i for i, x in enumerate(A)}
        longest = collections.defaultdict(lambda:2)
        ans = 0
        for k in range(len(A)):
            for j in range(k):
                i = index.get(A[k] - A[j],None)
                if i is not None and i < j:
                    longest[j,k] = longest[i,j] + 1
                    ans = max(ans,longest[j,k])
        return ans