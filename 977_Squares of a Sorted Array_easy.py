class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ans = []
        for tmp in A:
            ans.append(tmp**2)
        return sorted(ans)
        
——————————————————————————————————————————————
优先队列的做法
from Queue import PriorityQueue

class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ans = []
        Q = PriorityQueue()
        for tmp in A:
            Q.put(tmp**2)
            
        while not Q.empty():
            ans.append(Q.get())
        return ans
——————————————————————————————————————————————
堆的做法
import heapq

class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ans = []
        temp = []
        for tmp in A:
            temp.append(tmp**2)
        heapq.heapify(temp)
        for i in range(len(A)):
            ans.append(heapq.heappop(temp))
        return ans