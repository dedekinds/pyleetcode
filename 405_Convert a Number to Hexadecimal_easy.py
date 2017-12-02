'''
405. Convert a Number to Hexadecimal 
2017.12.2
'''
转换数字为16进制，如果是负数那么用补码表示
class Solution(object):
    def toHex(self, num):
        if num==0:
            return '0'
        ans=[]
        hexs='0123456789abcdef'
        if num < 0: 
            num += 0x100000000#32bits的负数取补码相当于加上2^32然后取16进制
        while num:
            ans.append(hexs[num % 16])
            num=num/16
        return ''.join(ans[::-1])
