import collections
class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        s = 0
        check = set()
        temp = collections.Counter([n%60 for n in time])
        for tmp in temp:
            if tmp==0 or tmp==30:
                s += int(temp[tmp]*(temp[tmp]-1)/2)
            else:
                if temp[60-tmp] and (tmp,60-tmp) not in check:
                    s += temp[tmp] * temp[60-tmp]
                    check.add((tmp,60-tmp))
                    check.add((60-tmp,tmp))
                    
        return s
                
        