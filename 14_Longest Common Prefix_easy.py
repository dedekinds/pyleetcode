
'''
14. Longest Common Prefix
2017.12.26
'''
最长公共前缀 O(min(strs_length))

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ''
        s=strs[0]
        ans=[]
        check=0
        for temp in range(len(strs[0])):
            for x in strs:
                if len(x)<temp+1 or s[temp] != x[temp]:
                    return ''.join(ans)
            ans.append(s[temp])
        return ''.join(ans)
                
                
        
