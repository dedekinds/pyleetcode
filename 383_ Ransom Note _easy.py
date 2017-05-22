'''383. Ransom Note  
   2017.5.22
   139ms
   beats 56.27%
'''
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomNote_nums=[0]*26
        magazine_nums=[0]*26
        for x in ransomNote:
            ransomNote_nums[ord(x)-97]+=1
        #print(ransomNote_nums)
        for y in magazine:
            magazine_nums[ord(y)-97]+=1
        #print(magazine_nums)
        for test in range(26):
            if ransomNote_nums[test]>magazine_nums[test]:
                return False
        return True


'''
best code
'''


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        if len(magazine) < len(ransomNote): return False
        
        set_r = set(ransomNote)
        
        for w in set_r:
            if ransomNote.count(w) > magazine.count(w):
                return False
        return True

