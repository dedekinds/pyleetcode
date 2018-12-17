惊人的思路：考虑每一个数位上1出现的可能个数
如31455先分为 a = 314   b = 55
例如按百位的数字分类讨论，当他分别为0,1,>=2三种情况讨论

当为0的时候完全取决于高位
当为1的时候取决于高位和低位
当大于等于2的时候取决于高位



https://www.nowcoder.com/profile/3547366/codeBookDetail?submissionId=9580864
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here221
        res = 0
        m = 1
        while m <= n:
            a = int(n/m)
            b = n%m
            
            temp = a%10
            if temp >= 2:res += (int(a/10)+1)*m
            if temp == 1:res += int(a/10)*m+(b+1)
            if temp == 0:res += int(a/10)*m
            m *= 10
        return res