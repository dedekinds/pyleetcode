'''500.Keyboard Row
   2017.5.16
   39ms
   beats 73.83%
'''
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        temp1=set(['q','w','e','r','t','y','u','i','o','p'])
        temp2=set(['a','s','d','f','g','h','j','k','l'])
        temp3=set(['z','x','c','v','b','n','m'])
        L=[]
        for x in words:
            temp=set(x.lower())
            judge1=temp&temp1==temp
            judge2=temp&temp2==temp
            judge3=temp&temp3==temp
            if judge1|judge2|judge3:
                L.append(x)
        return L