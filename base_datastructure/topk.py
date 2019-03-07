topk

heap:
import heapq
temp = [5,2,6,3,4]
建立堆:heapq.heapify(temp)
弹出顶:heqpq.heappop(temp)
压入堆:heapq.heappush(temp,2)

如果是要top max k 的话在压入的时候用 Push(-e)

import heapq
class Solution(object):
    def getLeastNumbers_Solution(self, input, k):
        """
        :type input: list[int]
        :type k: int
        :rtype: list[int]
        """
        heapq.heapify(input)
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(input))
        return ans
________________________________________________________
class Solution(object):
        
    def getLeastNumbers_Solution(self, input, k):
        """
        :type input: list[int]
        :type k: int
        :rtype: list[int]
        """
        def partition(array,l,r):
            x = array[r]
            i = l -1
            for j in range(l,r):
                if array[j] <= x:
                    i += 1
                    array[i],array[j] = array[j],array[i]
            array[r],array[i+1] = array[i+1],array[r]
            return i+1
        if not input or k <=0:return []
        if k>= len(input):return input
        l = 0
        r = len(input)-1
        index = partition(input,l,r)
        while index != k:
            if index > k-1:
                r = index - 1
                index = partition(input,l,r)
            else:
                l = index + 1
                index = partition(input,l,r)
        
        return input[:k]