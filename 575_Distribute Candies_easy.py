'''575. Distribute Candies 
   2017.5.15
   372ms
   beats 13.61%
'''
import itertools

class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        A=sorted(candies)
        num=0
        for key in itertools.groupby(A):
            num+=1
        if num>=len(candies)/2:
            return len(candies)/2
        else:
            return num
'''
The best code
55ms
'''
class Solution(object):
    def distributeCandies(self, candies):
        return min(len(set(candies)), len(candies) / 2)
        return sum(1 - v % 2 for v in collections.Counter(candies).values())