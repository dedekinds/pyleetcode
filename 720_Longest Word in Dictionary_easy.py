'''
720. Longest Word in Dictionary 
2017.12.4
'''
用set来构造关系链
class Solution():
    def longestWord(self, words):
        temp=set([''])# result:{''}
        ans=''
        for x in sorted(words):
            if x[:-1] in temp:
                temp.add(x)#temp.append(x)
                if len(x)>len(ans):
                    ans=x
        return ans
