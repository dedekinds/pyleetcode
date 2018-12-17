# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index == 0:return 0
        ugly = [1,2,3,4,5]
        index2 = 0
        index3 = 0
        index5 = 0
        if index <= 5:
            return ugly[index-1]
        cnt = 5
        while cnt <= index:
            temp = []#每次生成的三个数的大小不一定是按顺序的
            MAX =ugly[-1]
            t2 = MAX/2.0
            for i in range(index2,cnt):
                if ugly[i] > t2 :
                    temp.append(ugly[i]*2)
                    index2 = i
                    break
            t3 = MAX/3.0
            for i in range(index3,cnt):
                if ugly[i] > t3 :
                    temp.append(ugly[i]*3)
                    index3 = i
                    break
            t5 = MAX/5.0
            for i in range(index5,cnt):
                if ugly[i] > t5 :
                    temp.append(ugly[i]*5)
                    index5 = i
                    break

            ugly.append(min(temp))
            cnt += 1
        return ugly[index - 1]


————————————————————————————————————————————
另一种思路，和上面的思路相似，不过更加精确而已，最大的那个数newugly（每次生成的最小的那个数，也为新的ugly
这个数的t12 t3 t5可以精确找出
class Solution:
    def GetUglyNumber_Solution(self, index):
        if (index <= 0):
            return 0
        uglyList = [1]
        indexTwo = 0
        indexThree = 0
        indexFive = 0
        for i in range(index-1):
            newUgly = min(uglyList[indexTwo]*2, uglyList[indexThree]*3, uglyList[indexFive]*5)
            uglyList.append(newUgly)
            if (newUgly % 2 == 0):
                indexTwo += 1
            if (newUgly % 3 == 0):
                indexThree += 1
            if (newUgly % 5 == 0):
                indexFive += 1
        return uglyList[-1]