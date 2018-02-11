'''
781. Rabbits in Forest
2018.2.11
'''
class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        ans=0
        temp=collections.Counter(answers)
        for x in temp:
            if temp[x]%(x+1):
                ans+=(x+1)*(int(temp[x]/(x+1))+1)
            else:
                ans+=(x+1)*(int(temp[x]/(x+1)))    
        return ans
            