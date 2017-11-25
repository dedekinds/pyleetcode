'''
541. Reverse String II 
2017.11.26
'''
class Solution:
    def reverseStr(self, s, k):
        length=len(s)
        if length==0:
            return s
        if length<=k:
            return s[::-1]
        t=0
        while t<length:

            if t+k-1<length:
                s=s[0:t]+s[t:(t+k)][::-1]+s[t+k:]
                t=t+k
            else:
                s=s[:t]+s[t:][::-1]
            t+=k
        return s