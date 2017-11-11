'''
696. Count Binary Substrings 
2017.11.11
'''
#o(N)算法，http://bookshadow.com/weblog/2017/10/15/leetcode-count-binary-substrings/
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        cnt = [0, 0]
        last = None
        ans = 0
        for c in s:
            c = int(c)
            if c != last: cnt[c] = 0
            cnt[c] += 1
            if cnt[c] <= cnt[1 - c]: ans += 1#****!!!
            last = c
        return ans



___O(n2)暴力TLE____________
class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        temp=[0,0]
        for x in range(len(s)-1):
            temp[int(s[x])]+=1
            for y in range(x+1,len(s)):
                temp[int(s[y])]+=1
                if temp[0]==temp[1]:
                    #print(x,y)
                    ans+=1
                    temp=[0,0]
                    break
            temp=[0,0]
        return ans
            
