from Queue import PriorityQueue
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        Q = PriorityQueue()
        for tmp in points:
            Q.put((tmp[0]**2+tmp[1]**2,tmp[0],tmp[1]))
        ans = []
        for i in range(K):
            dis,x,y = Q.get()
            ans.append([x,y])
        return ans