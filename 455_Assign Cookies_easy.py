'''455. Assign Cookies  
   2017.7.10

'''
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        if len(s)==0:
            return 0
        g=sorted(g)
        s=sorted(s)
        ans=len(s)
        #模拟栈结构，大饼贪心给需求大的人
        while len(g)!=0 and len(s)!=0:
            if s[-1]>=g[-1]:
                s.pop()
                g.pop()
            else:
                g.pop()
        return ans-len(s)