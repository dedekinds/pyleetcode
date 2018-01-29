'''
260. Single Number III
2018.1.29
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #http://blog.csdn.net/yeruby/article/details/49853385
        #http://bookshadow.com/weblog/2015/08/17/leetcode-single-number-iii/
        #利用a&temp和b&temp的不同将数组分为两类，这两类由已知做异或运算就是a和b
        xor=reduce(lambda x,y: x^y, nums)
        temp=xor & -xor
        a=0
        b=0
        for x in nums:
            if x & temp:
                a=a^x
            else:
                b=b^x
        return [a,b]
                
        