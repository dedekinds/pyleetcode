'''
551. Student Attendance Record I 
2017.11.24
'''
class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return (s.count('A')<=1) and ('LLL' not in s)
        