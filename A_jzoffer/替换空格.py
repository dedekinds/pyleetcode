请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。 

# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        length = 0
        for i in s:
            if i == " ":length += 2
        pt1 = len(s)-1
        s = s + " "*(length)
        pt2 = len(s)-1
 
        temp = list(s)
        while (pt1 >= 0 and pt2 > pt1):
            if temp[pt1] != ' ':
                temp[pt2] = s[pt1]
                pt1 -= 1
                pt2 -= 1
            else:
                temp[pt2],temp[pt2-1],temp[pt2-2] = "0","2","%"
                pt1 -= 1
                pt2 -= 3
        return ''.join(temp)