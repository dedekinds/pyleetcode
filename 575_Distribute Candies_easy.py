'''575. Distribute Candies 
   2017.6.18
   228ms
   beats 35.53%
'''


class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        if int(len(candies)/2)>len(set(candies)):#直接考虑集合
            return len(set(candies))
        else:
            return int(len(candies)/2)


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
        for key in itertools.groupby(A):#强大的迭代器
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




2.groupby()把迭代器中相邻的重复元素挑出来放在一起：统计出现次数
import itertools
>>> for key, group in itertools.groupby('AAABBBCCAAA'):
...     print(key, list(group))
...
A ['A', 'A', 'A']
B ['B', 'B', 'B']
C ['C', 'C']
A ['A', 'A', 'A']