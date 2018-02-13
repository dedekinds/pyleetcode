'''
406. Queue Reconstruction by Height
2018.2.13
'''
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        #对people构建一个新的排序，排序规则如下：
        #1.先比较第一位，第一位大的在前面
        #2.如果第一位相同，那么第二位小的在前面
        #遍历新的排序后的people，ans.insert(x[1],x)
        def sort_rule(n1, n2):
            if n1[0]>n2[0]:
                return 1
            elif n1[0]==n2[0]:
                if n1[1]<=n2[1]:
                    return 1
                if n1[1]>n2[1]:
                    return -1
            if n1[0]<n2[0]:
                return -1
            else: return 0
        
        people.sort(sort_rule, reverse=True)
        
        ans=[]
        #print(people)
        for x in people:
            ans.insert(x[1],x)
        return ans