# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.s = ''
        self.tempcnt = {}
    def FirstAppearingOnce(self):
        # write code here
        for i in self.s:
            if i in self.tempcnt and self.tempcnt[i] == 1:
                return i
        return '#'
    def Insert(self, char):
        # write code here
        self.s += char
        if char in self.tempcnt:
            self.tempcnt[char] += 1
        else:self.tempcnt[char] = 1