'''
784. Letter Case Permutation
2018.2.22
'''
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        #temp.isalpha() 方法检测字符串是否只由字母组成。
        if not S:return [S]
        temp=self.letterCasePermutation(S[1:])
        if S[0].isalpha():
            return [S[0].upper() +s for s in temp]+[S[0].lower() +s for s in temp]
        else:
            return [S[0] + s for s in temp]
        