'''
717. 1-bit and 2-bit Characters 
2017.11.10
'''
class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if len(bits)==2 and bits[0]==1:
            return False
        x=0
        while x<len(bits):
            #print(x)
            if bits[x]==0 and x==len(bits)-1:
                return True
            if bits[x]==1:
                x+=2
                continue
            x+=1
        return False