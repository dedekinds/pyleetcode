'''338. Counting Bits 
   2017.6.24
   185ms
'''
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans=[0]
        for x in range(1,num+1):
            ans+=[ans[x>>1]+(x&1)]
        return ans

详细情况见自己CSDN博客文章
http://blog.csdn.net/qq_23997101/article/details/73692154