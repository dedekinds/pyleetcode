'''319. Bulb Switcher 
   2017.10.6
'''
实际上一开始是off，变化奇数次是on，偶数次是off
注意到变化次数实际上就是这个数的约数的个数，只有在完全平方数的时候才会是奇数次
所以实际上有多on就是问，1-n以内有多少个完全平方数
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.sqrt(n))
