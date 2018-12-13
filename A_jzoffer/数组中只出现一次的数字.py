根据全部的^获得一个数，找到这个数的二进制数的右边第一个1的位置，根据这个1的位置可以将数组分类
成两组，这样就可以分别对每一组都来一波^即可

# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def find_first_one(self,num):
        if num == 0:return -1
        cnt = 0
        while num:
            if num & 1:return cnt
            else:
                num = num >> 1
                cnt += 1
    def classifier(self,num,one_location):
        if (num >> one_location)%2 :return 1
        else:return 0
        
    def FindNumsAppearOnce(self, array):
        # write code here
        temp = array[0]
        for i in range(1,len(array)):
            temp = temp ^ array[i]
        one_location = self.find_first_one(temp)
        num1 = []
        num2 = []
        for i in range(len(array)):
            if (self.classifier(array[i],one_location))%2:num1.append(array[i])
            else:num2.append(array[i])
                
        a = num1[0]
        b = num2[0]
        for i in range(1,len(num1)):
            a = a ^ num1[i]
        for i in range(1,len(num2)):
            b = b ^ num2[i]
        return [a,b]
        
        
        
        
        