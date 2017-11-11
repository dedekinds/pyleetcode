'''
696. Count Binary Substrings 
2017.11.11
'''




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
            
