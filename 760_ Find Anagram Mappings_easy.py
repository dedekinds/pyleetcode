
'''
760. Find Anagram Mappings
2018.1.19
'''
class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        temp=dict()
        ans=[]
        for x in range(len(B)):
            temp[B[x]]=x
        for y in A:
            ans.append(temp[y])
        return ans