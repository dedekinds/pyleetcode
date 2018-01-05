
'''
190. Reverse Bits
2018.1.5
'''

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        temp= bin(n)[2:]
        binres=''.join(['0']*(32-len(temp)))+temp
        jw=1
        ans=0
        for x in binres:
            ans+=int(x)*jw
            jw*=2
        return ans
        