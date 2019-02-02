class Solution(object):
    def dfs(self,s,index,path,res):
        if index == len(s):
            res.append(path)
            return
        for i in range(index+1,len(s)+1):
            temp = s[index:i]
            if temp == temp[::-1]:
                self.dfs(s,i,path+[temp],res)
                
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.dfs(s,0,[],res)
        return res
        