'''
791. Custom Sort String
2018.2.25
'''
重载排序
class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        S = "cba"
        T = "abcd"
        """
        self.check=dict()
        for x in range(len(S)):
            self.check[S[x]]=x
            
        def comp(n1,n2):
            index1=-1
            index2=-1
            if n1 in self.check:index1=self.check[n1]
            if n2 in self.check:index2=self.check[n2]
                           
            if index1<index2:return -1
            elif index1>index2:return 1
            else:return 0
                        
        temp = [x for x in T]
        temp.sort(comp)
        #print(self.check)
        return ''.join(temp)

            
        
        
        