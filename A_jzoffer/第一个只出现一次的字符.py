# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code heredic
        hashset = {}
        for temp in s:
            if not temp in hashset.keys():hashset[temp] = 1
            else:hashset[temp] += 1
        for temp in range(len(s)):
            if hashset[s[temp]] == 1:return temp
        return -1