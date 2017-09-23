'''477. Total Hamming Distance 
   2017.9.23
'''

以题目案例为例
 4 is 0100, 14 is 1110, and 2 is 0010 
0100
1110
0010

考察倒数第二列
0
1
1
他们两两会产生2的汉明距离，实际上就是找多找对不同的 1-0，0有1个选择，1有2个选择
组合一共有2*1=2种，同样的我们可以遍历整个32位去得到所有的汉明距离
实际上就是找每一列中0和1的个数的乘积之和
————————————————————————
class Solution(object):
    def totalHammingDistance(self, nums):
        ans=0
        for i in range(32):
            mask=1<<i
            one=0
            zero=0
            for temp in nums:
                if temp&mask:
                    one+=1
                else:
                    zero+=1
            ans+=one*zero
        return ans
                    
