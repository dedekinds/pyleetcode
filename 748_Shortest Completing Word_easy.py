
'''
748. Shortest Completing Word
2017.12.17
'''
import collections
class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        letter=[chr(i) for i in range(65,91)]+[chr(i) for i in range(97,123)]#构造26*2个字母表
        license={}
        for x in licensePlate:
            x=x.lower()
            if x in letter:
                if x in license:#license表示的是licensePlate中所有字母构成的字典
                    license[x]+=1
                else:
                    license[x]=1
                    
        check=1
        ans=[]
        for x in words:#遍历words然后，每次都构造新的字典和license匹配
            temp=collections.Counter(list(x.lower()))
            for li in license.keys():
                if li not in temp:
                    check=0
                    break
                if license[li]>temp[li]:
                    check=0
                    break
            if check==1:
                if len(ans)==0:
                    ans.append(x)
                else:
                    if len(x)<len(ans[0]):
                        ans.pop()
                        ans.append(x)#更新最短的
            else:
                check=1
        return ans[0]
        
            
        
            