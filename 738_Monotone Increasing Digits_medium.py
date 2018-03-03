'''
738. Monotone Increasing Digits
2018.3.3
'''
class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
从高位向低位遍历整数N的各位数，找到第一个违反单调不减的数的下标x
将x位后的所有数替换为0，记得到的新数为M，则M - 1即为答案
        """
        temp=str(N)
        length=len(temp)
        now=False
        for x in range(length-1):
            if temp[x]>temp[x+1]:
                now=True
                break
        if not now:return N
        while x>0 and temp[x]==temp[x-1]:x-=1
        return int(temp[:(x+1)]+'0'*(length-x-1))-1